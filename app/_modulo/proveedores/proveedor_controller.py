from .proveedor_model import ProveedorModel

class ProveedorController:
    
    @staticmethod
    def get_all():
        try:
            proveedores = ProveedorModel.get_all()
            return proveedores if proveedores else []
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_one(id):
        try:
            proveedor = ProveedorModel(id=id).get_by_id()
            return proveedor if proveedor else {'error': 'Proveedor no encontrado'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['nombre', 'telefono', 'direccion', 'email']
            if not all(field in data for field in required_fields):
                return {'error': 'Faltan campos obligatorios'}
                
            proveedor = ProveedorModel(
                nombre=data['nombre'],
                telefono=data['telefono'],
                direccion=data['direccion'],
                email=data['email']
            )
            result = proveedor.create()
            return {'success': True, 'id': result} if result else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
                
            proveedor = ProveedorModel.deserializar(data)
            result = proveedor.update()
            return {'success': True} if result else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete(id):
        try:
            result = ProveedorModel.delete(id)
            return {'success': True} if result else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}