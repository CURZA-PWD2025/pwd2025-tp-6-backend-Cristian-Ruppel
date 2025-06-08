from .categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        try:
            return CategoriaModel.get_all()
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def get_one(id):
        try:
            categoria = CategoriaModel.get_one(id)
            return categoria if categoria else {'error': 'Categoría no encontrada'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def create(data):
        try:
            if not data.get('nombre'): 
                return {'error': 'Nombre es requerido'}
            categoria = CategoriaModel.deserializar(data)
            return {'success': True, 'id': categoria.id} if categoria.create() else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
            categoria = CategoriaModel.deserializar(data)
            return {'success': True} if categoria.update() else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def delete(id):
        try:
            return {'success': True} if CategoriaModel.delete(id) else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}