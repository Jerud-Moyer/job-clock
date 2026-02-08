from flask import Blueprint, request, jsonify
from app.models import Job
from app import db

job_controller = Blueprint('job_controller', __name__)

@job_controller.route('/say-hello')
def job():
    return {'message': 'Hello from the job controller!'}

@job_controller.route('/add-job', methods=['POST'])
def add_job():
    data = request.get_json()
    print(data)
    new_job = Job(
        title=data['title'],
        description=data.get('description', ''),
        client_id=data['client_id']
    )
    db.session.add(new_job)
    try:
        db.session.commit()
        return jsonify({'job': new_job.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@job_controller.route('/update-job/<int:job_id>/', methods=['PUT'])
def update_job(job_id):
    data = request.get_json()
    job = Job.query.get_or_404(job_id)

    job.title = data.get('title', job.title)
    job.description = data.get('description', job.description)
    job.active = data.get('active', job.active)
    job.client_id = data.get('client_id', job.client_id)
    job.last_clocked = data.get('last_clocked', job.last_clocked)

    db.session.add(job)
    try:
        db.session.commit()
        return jsonify(job.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@job_controller.route('/get-jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify({'jobs': [job.to_dict() for job in jobs]}), 200

@job_controller.route('/get-job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return jsonify(job.to_dict()), 200

@job_controller.route('/get-job-options', methods=['GET'])
def get_job_options():
    jobs = Job.query.all()
    options = [{'value': job.id, 'label': job.title} for job in jobs]
    return jsonify({'options': options}), 200

