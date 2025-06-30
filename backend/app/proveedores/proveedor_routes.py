from flask import Blueprint, jsonify, request
from .proveedor_controller import ProveedorController

proveedor_bp = Blueprint('proveedor', __name__, url_prefix='/api/proveedores')

@proveedor_bp.route('/', methods=['GET'])
def get_all():
    response = ProveedorController.get_all()
    return jsonify(response), response.get('status', 200)

@proveedor_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = ProveedorController.get_one(id)
    return jsonify(response), response.get('status', 200)

@proveedor_bp.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return jsonify({'error': 'Se requiere JSON', 'status': 400}), 400
    response = ProveedorController.create(request.get_json())
    return jsonify(response), response['status']

@proveedor_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    if not request.is_json:
        return jsonify({'error': 'Se requiere JSON', 'status': 400}), 400
    data = request.get_json()
    data['id'] = id
    response = ProveedorController.update(data)
    return jsonify(response), response['status']

@proveedor_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = ProveedorController.delete(id)
    return jsonify(response), response['status']