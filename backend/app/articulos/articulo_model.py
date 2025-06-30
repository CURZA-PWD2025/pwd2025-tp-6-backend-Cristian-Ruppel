from app.database.conect_db import ConectDB
from app.marcas.marca_model import MarcaModel
from app.proveedores.proveedor_model import ProveedorModel
from app.categorias.categoria_model import CategoriaModel

class ArticuloModel:
    def __init__(self, id=0, descripcion="", precio=0.0, stock=0, marca=None, proveedor=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca 
        self.proveedor = proveedor  
        self.categorias = categorias if categorias else []  

    def serializar(self, detalle_completo=False):
        """
        Versión flexible de serialización:
        - detalle_completo=False: Solo IDs para relaciones (para APIs)
        - detalle_completo=True: Objetos completos (para uso interno)
        """
        base = {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": float(self.precio),
            "stock": self.stock
        }
        
        if detalle_completo:
            base.update({
                "marca": self.marca.serializar() if self.marca else None,
                "proveedor": self.proveedor.serializar() if self.proveedor else None,
                "categorias": [cat.serializar() for cat in self.categorias] if self.categorias else []
            })
        else:
            base.update({
                "marca_id": self.marca.id if self.marca else None,
                "proveedor_id": self.proveedor.id if self.proveedor else None,
                "categoria_ids": [cat.id for cat in self.categorias]
            })
        
        return base

    @staticmethod
    def crear_desde_formulario(data):
        """Crea instancia validando datos del frontend"""
        try:
            required = ['descripcion', 'precio', 'stock', 'marca_id', 'proveedor_id']
            if not all(field in data for field in required):
                raise ValueError("Faltan campos obligatorios")

            marca_id = int(data['marca_id']) if data['marca_id'] else None
            proveedor_id = int(data['proveedor_id']) if data['proveedor_id'] else None
            categoria_ids = [int(cat_id) for cat_id in data.get('categoria_ids', []) if cat_id]

            marca = MarcaModel(id=marca_id) if marca_id else None
            proveedor = ProveedorModel(id=proveedor_id) if proveedor_id else None
            categorias = [CategoriaModel(id=cat_id) for cat_id in categoria_ids]

            return ArticuloModel(
                descripcion=data['descripcion'].strip(),
                precio=float(data['precio']),
                stock=int(data['stock']),
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )
        except (ValueError, TypeError) as e:
            raise ValueError(f"Datos inválidos: {str(e)}")
