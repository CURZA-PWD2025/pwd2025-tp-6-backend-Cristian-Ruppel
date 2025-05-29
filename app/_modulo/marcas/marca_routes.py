from flask import Blueprint, jsonify, request
from .marca_controller import MarcaController

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/marcas', methods=['GET'])
def get_all():
    response = MarcaController.get_all()
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'No hay marcas'}), 404

@marca_bp.route('/marcas/<int:id>', methods=['GET'])
def get_one(id):
    response = MarcaController.get_one(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'Marca no encontrada'}), 404

@marca_bp.route('/marcas', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = MarcaController.create(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca creada', 'id': response}), 201

@marca_bp.route('/marcas/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = MarcaController.update(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca actualizada'}), 200

@marca_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete(id):
    response = MarcaController.delete(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Marca eliminada'}), 200