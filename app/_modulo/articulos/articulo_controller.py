from app._modulo.database.conect_db import ConectDB
from app._modulo.articulos.articulo_model import ArticuloModel
from app._modulo.marcas.marca_model import MarcaModel
from app._modulo.proveedores.proveedor_model import ProveedorModel
from app._modulo.categorias.categoria_model import CategoriaModel

class ArticuloController:
    
    @staticmethod
    def get_all():
        try:
            articulos = ArticuloModel.get_all()
            return [articulo.serializar() for articulo in articulos] if articulos else []
        except Exception as e:
            print(f"Error en ArticuloController.get_all: {str(e)}")
            return {'error': 'Error al obtener artículos', 'detalle': str(e)}
    
    @staticmethod
    def get_one(id):
        try:
            articulo = ArticuloModel.get_by_id(id)
            if not articulo:
                return {'error': 'Artículo no encontrado'}
            return articulo.serializar()
        except Exception as e:
            print(f"Error en ArticuloController.get_one: {str(e)}")
            return {'error': 'Error al obtener artículo', 'detalle': str(e)}
    
    @staticmethod
    def create(data):
        try:
            required_fields = ['descripcion', 'precio', 'stock', 'marca_id', 'proveedor_id']
            if not all(field in data for field in required_fields):
                return {'error': 'Faltan campos obligatorios'}
            
            articulo = ArticuloModel(
                descripcion=data['descripcion'],
                precio=float(data['precio']),
                stock=int(data['stock']),
                marca_id=data['marca_id'],
                proveedor_id=data['proveedor_id']
            )
            
            if articulo.create():
                return {'success': True, 'id': articulo.id}
            return {'error': 'No se pudo crear el artículo'}
            
        except Exception as e:
            print(f"Error en ArticuloController.create: {str(e)}")
            return {'error': 'Error al crear artículo', 'detalle': str(e)}
    
    @staticmethod
    def update(data):
        try:
            if 'id' not in data:
                return {'error': 'ID de artículo no especificado'}
                
            articulo = ArticuloModel(
                id=data['id'],
                descripcion=data.get('descripcion'),
                precio=data.get('precio'),
                stock=data.get('stock'),
                marca_id=data.get('marca_id'),
                proveedor_id=data.get('proveedor_id')
            )
            
            if articulo.update():
                return {'success': True}
            return {'error': 'No se pudo actualizar el artículo'}
            
        except Exception as e:
            print(f"Error en ArticuloController.update: {str(e)}")
            return {'error': 'Error al actualizar artículo', 'detalle': str(e)}
    
    @staticmethod
    def delete(id):
        try:
            if ArticuloModel.delete(id):
                return {'success': True}
            return {'error': 'No se pudo eliminar el artículo'}
        except Exception as e:
            print(f"Error en ArticuloController.delete: {str(e)}")
            return {'error': 'Error al eliminar artículo', 'detalle': str(e)}