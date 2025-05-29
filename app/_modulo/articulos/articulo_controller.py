from .articulo_model import ArticuloModel
from ..marca.marca_model import MarcaModel
from ..proveedor.proveedor_model import ProveedorModel
from ..categoria.categoria_model import CategoriaModel
from ...database.conect_db import ConectDB

class ArticuloController:
    
    @staticmethod
    def get_all():
        """Obtiene todos los artículos"""
        try:
            articulos = ArticuloModel.get_all()
            return articulos if articulos else []
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_one(id):
        """Obtiene un artículo específico por ID"""
        try:
            articulo = ArticuloModel(id=id).get_by_id()
            return articulo if articulo else None
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def create(data):
        """Crea un nuevo artículo"""
        try:
            articulo = ArticuloModel(
                descripcion=data['descripcion'],
                precio=data['precio'],
                stock=data['stock'],
                marca_id=data['marca_id'],
                proveedor_id=data['proveedor_id']
            )
            result = articulo.create()
            return {'success': True, 'id': result} if result else {'error': 'No se pudo crear'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def update(data):
        """Actualiza un artículo existente"""
        try:
            articulo = ArticuloModel.deserializar(data)
            result = articulo.update()
            return {'success': True} if result else {'error': 'No se pudo actualizar'}
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def delete(id):
        """Elimina un artículo por ID"""
        try:
            result = ArticuloModel.delete(id)
            return {'success': True} if result else {'error': 'No se pudo eliminar'}
        except Exception as e:
            return {'error': str(e)}