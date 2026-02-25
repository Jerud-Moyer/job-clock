from flask import Blueprint, request, jsonify
from app.models import TimeEntry, Client, Job
from app import db
# import urllib.request as request
from datetime import timedelta
import threading, os

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

    c_id = db.session.query(Job).filter(Job.id == data['job_id']).first().client_id

    entry.start_time = data.get('start_time', entry.start_time)
    entry.end_time = data.get('end_time', entry.end_time)
    entry.notes = data.get('notes', entry.notes)
    entry.client_id = c_id
    entry.job_id = data.get('job_id', entry.job_id)
    entry.currently_open = False

    db.session.add(entry)

    try:
        db.session.commit()
        return jsonify({'time_entry': entry.to_dict()}), 200
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

@clock_controller.route('/check-for-open-entry')
def check_for_open():
    entry = db.session.query(TimeEntry).filter_by(currently_open=True).first()
    # send found entry or null
    if entry is not None:
        return jsonify({'time_entry': entry.to_dict()}), 200
    
    return jsonify({'time_entry': None}), 200

@clock_controller.route('/get-entries-by-job')
def get_entries_by_job(id):
    entries = db.session.query(TimeEntry).filter_by(job_id=id).all()
    return jsonify({'time_entries': [entry.to_dict() for entry in entries]}), 200

@clock_controller.route('/get-entries-by-date', methods=['POST'])
def get_entries_by_date():
    data = request.get_json()

    entries_in_range = db.session.query(TimeEntry).filter(
        TimeEntry.start_time >= data['start_time'],
        TimeEntry.end_time <= data['end_time'],
        TimeEntry.end_time != TimeEntry.start_time
    ).all()

    total_hours = timedelta()

    for entry in entries_in_range:
        hours = entry.end_time - entry.start_time
        total_hours += hours

    return jsonify({
        'time_entries': [entry.to_dict() for entry in entries_in_range],
        'total_hours': str(total_hours)    
    }), 200

@clock_controller.route('/get-filtered-entries', methods=['POST'])
def get_filtered_entries():
    data = request.get_json()

    query = db.session.query(TimeEntry).filter(
        TimeEntry.start_time >= data['start_time'],
        TimeEntry.end_time <= data['end_time'],
        TimeEntry.end_time != TimeEntry.start_time
    )

    other_filters = {
        'client_id': TimeEntry.client_id,
        'job_id': TimeEntry.job_id
    }

    for key, model_val in other_filters.items():
        if key in data:
            query = query.filter(model_val == data[key])

    filtered_entries = query.all()

    total_hours = timedelta()

    for entry in filtered_entries:
        hours = entry.end_time - entry.start_time
        total_hours += hours

    return jsonify({
        'time_entries': [entry.to_dict() for entry in filtered_entries],
        'total_hours': str(total_hours)    
    }), 200

@clock_controller.route('/get-entry-by-id/<int:id>')
def get_entry_by_id(id):
    entry = TimeEntry.query.get_or_404(id)
    return jsonify({'time_entry': entry.to_dict()})

@clock_controller.route('/get-entries-by-client')
def get_entries_by_client(id):
    entries = db.session.query(TimeEntry).filter_by(client_id=id).all()
    return jsonify({'time_entries': [entry.to_dict() for entry in entries]}), 200

@clock_controller.route('/delete-entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    entry = TimeEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    try:
        db.session.commit()
        return jsonify({'message': 'Entry deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
