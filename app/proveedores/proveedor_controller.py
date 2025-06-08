from .proveedor_model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        try:
            return ProveedorModel.get_all()
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def get_one(id):
        try:
            proveedor = ProveedorModel.get_one(id)
            return proveedor if proveedor else {'error': 'Proveedor no encontrado'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def create(data):
        try:
            required_fields = ['nombre', 'telefono', 'direccion', 'email']
            if not all(field in data for field in required_fields):
                return {'error': 'Faltan campos obligatorios'}
                
            proveedor = ProveedorModel.deserializar(data)
            return {'success': True, 'id': proveedor.id} if proveedor.create() else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
                
            proveedor = ProveedorModel.deserializar(data)
            return {'success': True} if proveedor.update() else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def delete(id):
        try:
            return {'success': True} if ProveedorModel.delete(id) else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}