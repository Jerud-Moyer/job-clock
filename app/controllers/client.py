from flask import Blueprint, request, jsonify
from ..models import Client

client_controller = Blueprint('client_controller', __name__)

@client_controller.route('/say-hello')
def client():
    return {'message': 'Hello from the client controller!'}

@client_controller.route('/add-client', methods=['POST'])
def add_client():
    data = request.get_json()
    new_client = Client(name=data['name'],
                        email=data['email'],
                        phone=data.get('phone'),
                        address=data.get('address'))
    try:
        new_client.save()
        return jsonify(new_client.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@client_controller.route('/get-clients', methods=['GET'])   
def get_clients():
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients]), 200

@client_controller.route('/get-client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify(client.to_dict()), 200

@client_controller.route('/update-client/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    client = Client.query.get_or_404(client_id)
    
    client.name = data.get('name', client.name)
    client.email = data.get('email', client.email)
    client.phone = data.get('phone', client.phone)
    client.address = data.get('address', client.address)
    
    try:
        client.save()
        return jsonify(client.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400