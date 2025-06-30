from app.articulos.articulo_model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        try:
            articulos = ArticuloModel.get_all()
            return [art.serializar() for art in articulos] if articulos else []
        except Exception as e:
            return {'error': str(e), 'status': 500}
    
    @staticmethod
    def get_one(id):
        try:
            articulo = ArticuloModel.get_one(id)
            return articulo.serializar() if articulo else {'error': 'Artículo no encontrado', 'status': 404}
        except Exception as e:
            return {'error': str(e), 'status': 500}
    
    @staticmethod
    def create(data):
        try:
            articulo = ArticuloModel.crear_desde_formulario(data)
            if articulo.create():
                return {'success': True, 'id': articulo.id, 'data': articulo.serializar(), 'status': 201}
            return {'error': 'Error al crear artículo', 'status': 400}
        except ValueError as e:
            return {'error': str(e), 'status': 400}
        except Exception as e:
            return {'error': f"Error interno: {str(e)}", 'status': 500}
    
    @staticmethod
    def update(data):
        try:
            if 'id' not in data:
                return {'error': 'ID de artículo no especificado', 'status': 400}
                
            articulo = ArticuloModel.crear_desde_formulario(data)
            if articulo.update():
                return {'success': True, 'data': articulo.serializar(), 'status': 200}
            return {'error': 'Error al actualizar artículo', 'status': 400}
        except ValueError as e:
            return {'error': str(e), 'status': 400}
        except Exception as e:
            return {'error': f"Error interno: {str(e)}", 'status': 500}
    
    @staticmethod
    def delete(id):
        try:
            if ArticuloModel.delete(id):
                return {'success': True, 'status': 200}
            return {'error': 'Error al eliminar artículo', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}