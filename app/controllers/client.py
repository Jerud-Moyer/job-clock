from flask import Blueprint, request, jsonify
from app.models import Client
from app import db

client_controller = Blueprint('client_controller', __name__)

@client_controller.route('/say-hello')
def client():
    return {'message': 'Hello from the client controller!'}

@client_controller.route('/add-client', methods=['POST'])
def add_client():
    data = request.get_json()
    new_client = Client(first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        phone=data['phone'],
                        street_address=data['street_address'],
                        city=data['city'],
                        state=data['state'],
                        zip_code=data['zip_code'],
                        current_rate=data['current_rate']
                        )
    db.session.add(new_client)
    try:
        db.session.commit()
        return jsonify({'client': new_client.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@client_controller.route('/get-clients', methods=['GET'])   
def get_clients():
    clients = Client.query.all()
    return jsonify({'clients': [client.to_dict() for client in clients]}), 200

@client_controller.route('/get-client/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify(client.to_dict()), 200

@client_controller.route('/update-client/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    print("Updating client with ID:", client_id)
    data = request.get_json()
    client = Client.query.get_or_404(client_id)
    
    client.first_name = data.get('first_name', client.first_name)
    client.last_name = data.get('last_name', client.last_name)
    client.email = data.get('email', client.email)
    client.phone = data.get('phone', client.phone)
    client.street_address = data.get('street_address', client.street_address)
    client.city = data.get('city', client.city)
    client.state = data.get('state', client.state)
    client.zip_code = data.get('zip_code', client.zip_code)
    client.current_rate = data.get('current_rate', client.current_rate)
    
    db.session.add(client)
    try:
        db.session.commit()
        return jsonify(client.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@client_controller.route('/delete-client/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    try:
        client.delete()
        return jsonify({'message': 'Client deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@client_controller.route('/get-client-options', methods=['GET'])
def get_client_options():
    clients = Client.query.all()
    options = [{'value': client.id, 'label': f"{client.first_name} {client.last_name}"} for client in clients]
    return jsonify({'options': options}), 200