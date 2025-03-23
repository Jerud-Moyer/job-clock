from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/say-hello')
def say_it():
  return {'Hello': 'World'} 
