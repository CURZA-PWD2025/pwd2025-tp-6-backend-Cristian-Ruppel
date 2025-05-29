from flask import Blueprint, jsonify, request
from .articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo', __name__)

@articulo_bp.route('/articulos', methods=['GET'])
def get_all():
    response = ArticuloController.get_all()
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'No hay artículos'}), 404

@articulo_bp.route('/articulos/<int:id>', methods=['GET'])
def get_one(id):
    response = ArticuloController.get_one(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'Artículo no encontrado'}), 404

@articulo_bp.route('/articulos', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = ArticuloController.create(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo creado', 'id': response}), 201

@articulo_bp.route('/articulos/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = ArticuloController.update(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo actualizado'}), 200

@articulo_bp.route('/articulos/<int:id>', methods=['DELETE'])
def delete(id):
    response = ArticuloController.delete(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo eliminado'}), 200