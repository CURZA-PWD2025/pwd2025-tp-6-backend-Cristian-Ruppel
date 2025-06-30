from flask import Blueprint, jsonify, request
from ..articulos.articulo_controller import ArticuloController

articulo_bp = Blueprint('articulo', __name__, url_prefix='/api/articulos')

def _validate_json():
    if not request.is_json:
        return None
    return request.get_json()

@articulo_bp.route('/', methods=['GET'])
def get_all():
    response = ArticuloController.get_all()
    return jsonify(response), response.get('status', 200)

@articulo_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = ArticuloController.get_one(id)
    return jsonify(response), response.get('status', 200)

@articulo_bp.route('/', methods=['POST'])
def create():
    if not (data := _validate_json()):
        return jsonify({'error': 'Se requieren datos JSON', 'status': 400}), 400
    
    response = ArticuloController.create(data)
    return jsonify(response), response['status']

@articulo_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    if not (data := _validate_json()):
        return jsonify({'error': 'Se requieren datos JSON', 'status': 400}), 400
    
    data['id'] = id
    response = ArticuloController.update(data)
    return jsonify(response), response['status']

@articulo_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = ArticuloController.delete(id)
    return jsonify(response), response['status']