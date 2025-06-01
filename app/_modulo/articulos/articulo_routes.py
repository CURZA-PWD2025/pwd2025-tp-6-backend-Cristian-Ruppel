from flask import Blueprint, jsonify, request
from .articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo', __name__)

@articulo_bp.route('/', methods=['GET'])
def get_all():
    response = ArticuloController.get_all()
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response if response else []), 200


@articulo_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = ArticuloController.get_one(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 404 if response['error'] == 'Artículo no encontrado' else 500
    return jsonify(response), 200

@articulo_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    response = ArticuloController.create(data)
    return jsonify(response), 201 if 'success' in response else 400

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    data['id'] = id
    response = ArticuloController.update(data)
    return jsonify(response), 200 if 'success' in response else 400

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = ArticuloController.delete(id)
    return jsonify(response), 200 if 'success' in response else 400