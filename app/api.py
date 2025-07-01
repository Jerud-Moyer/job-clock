from flask import Blueprint
from .controllers.client import client_controller
from .controllers.job import job_controller

api = Blueprint('api', __name__)
api.register_blueprint(client_controller, url_prefix='/clients')
api.register_blueprint(job_controller, url_prefix='/jobs')

@api.route('/say-hello')
def say_it():
  return {'Hello': 'World'} 
