from flask import Blueprint, jsonify, request
from .proveedor_controller import ProveedorController

proveedor_bp = Blueprint('proveedor', __name__, url_prefix='/api/proveedores')

@proveedor_bp.route('/', methods=['GET'])
def get_all():
    response = ProveedorController.get_all()
    if 'error' in response:
        return jsonify(response), 500
    return jsonify(response), 200

@proveedor_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    response = ProveedorController.get_one(id)
    if 'error' in response:
        return jsonify(response), 404 if response['error'] == 'Proveedor no encontrado' else 500
    return jsonify(response), 200

@proveedor_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = ProveedorController.create(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor creado', 'id': response['id']}), 201

@proveedor_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = ProveedorController.update(data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor actualizado'}), 200

@proveedor_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    response = ProveedorController.delete(id)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor eliminado'}), 200