from flask import Blueprint, request, jsonify
from app.models import TimeEntry, Client, Job
from app import db

clock_controller = Blueprint('clock_controller', __name__)

@clock_controller.route('/add-entry', methods=['POST'])
def add_entry():
    data = request.get_json()

    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")

    c_id = db.session.query(Job).filter(Job.id == data['job_id']).first().client_id
    previously_working = db.session.query(TimeEntry).filter(TimeEntry.currently_open == True).first()

    if previously_working is not None:
        previously_working.currently_open = False
        previously_working.end_time = data['start_time']
        db.session.add(previously_working)

    new_entry = TimeEntry(
        start_time = data['start_time'],
        end_time = data.get('end_time', data.get('start_time')),
        notes = data.get('notes', ''),
        client_id = c_id,
        job_id = data['job_id'],
        currently_open = True
    )

    db.session.add(new_entry)
    try:
        db.session.commit()
        return jsonify({'time_entry': new_entry.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@clock_controller.route('/update-entry/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.get_json()
    entry = TimeEntry.query.get_or_404(entry_id)

    entry.start_time = data.get('start_time', entry.start_time)
    entry.end_time = data.get('end_time', entry.end_time)
    entry.notes = data.get('notes', entry.notes)
    entry.client_id = data.get('client_id', entry.client_id)
    entry.job_id = data.get('job_id', entry.job_id)
    entry.currently_open = False

    db.session.add(new_entry)

    try:
        db.session.commit()
        return jsonify({'time_entry': new_entry.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@clock_controller.route('/clock-out/<int:entry_id>', methods=['PUT'])
def clock_out(entry_id):
    entry = TimeEntry.query.get_or_404(entry_id)
    data = request.get_json()
    entry.end_time = data['end_time']
    entry.currently_open = False

    db.session.add(entry)

    try:
        db.session.commit()
        return jsonify({'time_entry': entry.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@clock_controller.route('/get-entries-by-job')
def get_entries_by_job(id):
    entries = session.query(TimeEntry).filter_by(job_id=id).all()
    return jsonify({'time_entries': [entry.to_dict() for entry in entries]}), 200

@clock_controller.route('/get-entries-by-client')
def get_entries_by_client(id):
    entries = session.query(TimeEntry).filter_by(client_id=id).all()
    return jsonify({'time_entries': [entry.to_dict() for entry in entries]}), 200

@clock_controller.route('/delete-entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    entry = TimeEntry.query.get_or_404(entry_id)
    try:
        entry.delete()
        return jsonify({'message': 'Entry deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400