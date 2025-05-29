from flask import Blueprint, jsonify, request
from .categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route('/categorias', methods=['GET'])
def get_all():
    response = CategoriaController.get_all()
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'No hay categorías'}), 404

@categoria_bp.route('/categorias/<int:id>', methods=['GET'])
def get_one(id):
    response = CategoriaController.get_one(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'Categoría no encontrada'}), 404

@categoria_bp.route('/categorias', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = CategoriaController.create(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría creada', 'id': response}), 201

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = CategoriaController.update(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría actualizada'}), 200

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete(id):
    response = CategoriaController.delete(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría eliminada'}), 200