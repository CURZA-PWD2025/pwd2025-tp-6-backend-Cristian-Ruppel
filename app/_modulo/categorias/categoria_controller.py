from .categoria_model import CategoriaModel

class CategoriaController:
    
    @staticmethod
    def get_all():
        try:
            categorias = CategoriaModel.get_all()
            return categorias if categorias else []
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_one(id):
        try:
            categoria = CategoriaModel(id=id).get_by_id()
            return categoria if categoria else {'error': 'Categoría no encontrada'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def create(data):
        try:
            if not data.get('descripcion'):
                return {'error': 'Descripción es requerida'}
                
            categoria = CategoriaModel(descripcion=data['descripcion'])
            result = categoria.create()
            return {'success': True, 'id': result} if result else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
                
            categoria = CategoriaModel.deserializar(data)
            result = categoria.update()
            return {'success': True} if result else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete(id):
        try:
            result = CategoriaModel.delete(id)
            return {'success': True} if result else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}