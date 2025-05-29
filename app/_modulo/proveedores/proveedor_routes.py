from flask import Blueprint, jsonify, request
from .proveedor_controller import ProveedorController

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route('/proveedores', methods=['GET'])
def get_all():
    response = ProveedorController.get_all()
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'No hay proveedores'}), 404

@proveedor_bp.route('/proveedores/<int:id>', methods=['GET'])
def get_one(id):
    response = ProveedorController.get_one(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 500
    return jsonify(response) if response else jsonify({'mensaje': 'Proveedor no encontrado'}), 404

@proveedor_bp.route('/proveedores', methods=['POST'])
def create():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    response = ProveedorController.create(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor creado', 'id': response}), 201

@proveedor_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    data['id'] = id
    response = ProveedorController.update(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor actualizado'}), 200

@proveedor_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete(id):
    response = ProveedorController.delete(id)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), 400
    return jsonify({'mensaje': 'Proveedor eliminado'}), 200