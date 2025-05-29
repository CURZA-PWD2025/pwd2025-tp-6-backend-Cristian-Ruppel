from .marca_model import MarcaModel

class MarcaController:
    
    @staticmethod
    def get_all():
        try:
            marcas = MarcaModel.get_all()
            return marcas if marcas else []
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_one(id):
        try:
            marca = MarcaModel(id=id).get_by_id()
            return marca if marca else {'error': 'Marca no encontrada'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def create(data):
        try:
            if not data.get('descripcion'):
                return {'error': 'Descripción es requerida'}
                
            marca = MarcaModel(descripcion=data['descripcion'])
            result = marca.create()
            return {'success': True, 'id': result} if result else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
                
            marca = MarcaModel.deserializar(data)
            result = marca.update()
            return {'success': True} if result else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete(id):
        try:
            result = MarcaModel.delete(id)
            return {'success': True} if result else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}