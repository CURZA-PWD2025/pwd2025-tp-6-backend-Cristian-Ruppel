from flask import Blueprint, jsonify, request
from .marca_controller import MarcaController

marca_bp = Blueprint('marca', __name__, url_prefix='/api/marcas')

@marca_bp.route('/', methods=['GET'])
def get_all():
    response = MarcaController.get_all()
    if 'error' in response:
        return jsonify(response), 500
    return jsonify(response), 200

@marca_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = MarcaController.get_one(id)
    if 'error' in response:
        return jsonify(response), 404 if response['error'] == 'Marca no encontrada' else 500
    return jsonify(response), 200

@marca_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = MarcaController.create(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca creada', 'id': response['id']}), 201

@marca_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = MarcaController.update(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca actualizada'}), 200

@marca_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = MarcaController.delete(id)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca eliminada'}), 200