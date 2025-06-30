from .categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        try:
            categorias = CategoriaModel.get_all()
            return [c.serializar() for c in categorias] if categorias else []
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def get_one(id):
        try:
            if categoria := CategoriaModel.get_one(id):
                return categoria.serializar()
            return {'error': 'Categoría no encontrada', 'status': 404}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def create(data):
        try:
            if not data.get('nombre'):
                return {'error': 'Nombre es requerido', 'status': 400}
            categoria = CategoriaModel.deserializar(data)
            if categoria.create():
                return {'success': True, 'id': categoria.id, 'status': 201}
            return {'error': 'Error al crear categoría', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido', 'status': 400}
            categoria = CategoriaModel.deserializar(data)
            if categoria.update():
                return {'success': True, 'status': 200}
            return {'error': 'Error al actualizar categoría', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def delete(id):
        try:
            if CategoriaModel.delete(id):
                return {'success': True, 'status': 200}
            return {'error': 'Error al eliminar categoría', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}