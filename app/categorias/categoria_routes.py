from flask import Blueprint, jsonify, request
from .categoria_controller import CategoriaController

categoria_bp = Blueprint('categoria', __name__, url_prefix='/api/categorias')

@categoria_bp.route('/', methods=['GET'])
def get_all():
    response = CategoriaController.get_all()
    if 'error' in response:
        return jsonify(response), 500
    return jsonify(response), 200

@categoria_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = CategoriaController.get_one(id)
    if 'error' in response:
        return jsonify(response), 404 if response['error'] == 'Categoría no encontrada' else 500
    return jsonify(response), 200

@categoria_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = CategoriaController.create(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría creada', 'id': response['id']}), 201

@categoria_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = CategoriaController.update(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría actualizada'}), 200

@categoria_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = CategoriaController.delete(id)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Categoría eliminada'}), 200