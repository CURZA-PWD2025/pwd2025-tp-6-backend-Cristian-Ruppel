from .articulo_model import ArticuloModel

class ArticuloController:
    @staticmethod
    def get_all():
        try:
            articulos = ArticuloModel.get_all()
            return articulos if articulos else []
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_one(id):
        try:
            articulo = ArticuloModel.get_one(id)
            return articulo if articulo else {'error': 'Artículo no encontrado'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['descripcion', 'precio', 'stock', 'marca', 'proveedor']
            if not all(field in data for field in required_fields):
                return {'error': 'Faltan campos obligatorios'}
                
            articulo = ArticuloModel.deserializar(data)
            if articulo.create():
                return {'success': True, 'id': articulo.id}
            return {'error': 'Error al crear artículo'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update(data):
        try:
            if 'id' not in data:
                return {'error': 'ID de artículo no especificado'}
                
            articulo = ArticuloModel.deserializar(data)
            if articulo.update():
                return {'success': True}
            return {'error': 'Error al actualizar artículo'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete(id):
        try:
            if ArticuloModel.delete(id):
                return {'success': True}
            return {'error': 'Error al eliminar artículo'}
        except Exception as e:
            return {'error': str(e)}