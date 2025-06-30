from flask import Blueprint, jsonify, request
from .marca_controller import MarcaController

marca_bp = Blueprint('marca', __name__, url_prefix='/api/marcas')

@marca_bp.route('/', methods=['GET'])
def get_all():
    response = MarcaController.get_all()
    return jsonify(response), response.get('status', 200)

@marca_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = MarcaController.get_one(id)
    return jsonify(response), response.get('status', 200)

@marca_bp.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return jsonify({'error': 'Se requiere JSON', 'status': 400}), 400
    response = MarcaController.create(request.get_json())
    return jsonify(response), response['status']

@marca_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    if not request.is_json:
        return jsonify({'error': 'Se requiere JSON', 'status': 400}), 400
    data = request.get_json()
    data['id'] = id
    response = MarcaController.update(data)
    return jsonify(response), response['status']

@marca_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = MarcaController.delete(id)
    return jsonify(response), response['status']