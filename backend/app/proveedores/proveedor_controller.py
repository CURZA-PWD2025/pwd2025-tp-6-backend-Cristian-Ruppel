from .proveedor_model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        try:
            proveedores = ProveedorModel.get_all()
            return [p.serializar() for p in proveedores] if proveedores else []
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def get_one(id):
        try:
            if proveedor := ProveedorModel.get_one(id):
                return proveedor.serializar()
            return {'error': 'Proveedor no encontrado', 'status': 404}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def create(data):
        try:
            required = ['nombre', 'telefono', 'direccion', 'email']
            if not all(field in data for field in required):
                return {'error': 'Faltan campos obligatorios', 'status': 400}
                
            proveedor = ProveedorModel.deserializar(data)
            if proveedor.create():
                return {'success': True, 'id': proveedor.id, 'status': 201}
            return {'error': 'Error al crear proveedor', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido', 'status': 400}
                
            proveedor = ProveedorModel.deserializar(data)
            if proveedor.update():
                return {'success': True, 'status': 200}
            return {'error': 'Error al actualizar proveedor', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def delete(id):
        try:
            if ProveedorModel.delete(id):
                return {'success': True, 'status': 200}
            return {'error': 'Error al eliminar proveedor', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}