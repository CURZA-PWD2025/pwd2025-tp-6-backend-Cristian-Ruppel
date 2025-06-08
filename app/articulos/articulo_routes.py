from flask import Blueprint, jsonify, request
from .articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo', __name__, url_prefix='/api/articulos')

@articulo_bp.route('/', methods=['GET'])
def get_all():
    response = ArticuloController.get_all()
    if 'error' in response:
        return jsonify(response), 500
    return jsonify(response), 200

@articulo_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = ArticuloController.get_one(id)
    if 'error' in response:
        return jsonify(response), 404
    return jsonify(response), 200

@articulo_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
        
    response = ArticuloController.create(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo creado', 'id': response['id']}), 201

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
        
    data['id'] = id
    response = ArticuloController.update(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo actualizado'}), 200

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = ArticuloController.delete(id)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Artículo eliminado'}), 200