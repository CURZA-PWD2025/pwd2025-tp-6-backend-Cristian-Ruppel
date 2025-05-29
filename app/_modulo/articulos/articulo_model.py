from ...database.conect_db import ConectDB
from ..marca.marca_model import MarcaModel
from ..proveedor.proveedor_model import ProveedorModel
from ..categoria.categoria_model import CategoriaModel

class ArticuloModel:
    def __init__(self, id=0, descripcion="", precio=0.0, stock=0, marca=None, proveedor=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias if categorias is not None else []

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serialize() if self.marca else None,
            "proveedor": self.proveedor.serialize() if self.proveedor else None,
            "categorias": [c.serialize() for c in self.categorias] if self.categorias else []
        }

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS")
                articulos = []
                for row in cursor.fetchall():
                    marca = MarcaModel(id=row['marca_id']).get_by_id()
                    proveedor = ProveedorModel(id=row['proveedor_id']).get_by_id()
                    
                    cursor.execute("""
                        SELECT c.* FROM CATEGORIAS c
                        JOIN ARTICULOS_CATEGORIAS ac ON c.id = ac.categoria_id
                        WHERE ac.articulo_id = %s
                    """, (row['id'],))
                    
                    categorias = [CategoriaModel(**c).serialize() for c in cursor.fetchall()]
                    
                    articulos.append({
                        "id": row['id'],
                        "descripcion": row['descripcion'],
                        "precio": row['precio'],
                        "stock": row['stock'],
                        "marca": marca,
                        "proveedor": proveedor,
                        "categorias": categorias
                    })
                return articulos
        except Exception as e:
            print(f"Error en get_all: {str(e)}")
            return None
        finally:
            cnx.close()

    @staticmethod
    def get_by_id(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
                row = cursor.fetchone()
                if not row:
                    return None
                
                marca = MarcaModel(id=row['marca_id']).get_by_id()
                proveedor = ProveedorModel(id=row['proveedor_id']).get_by_id()
                
                cursor.execute("""
                    SELECT c.* FROM CATEGORIAS c
                    JOIN ARTICULOS_CATEGORIAS ac ON c.id = ac.categoria_id
                    WHERE ac.articulo_id = %s
                """, (id,))
                
                categorias = [CategoriaModel(**c).serialize() for c in cursor.fetchall()]
                
                return {
                    "id": row['id'],
                    "descripcion": row['descripcion'],
                    "precio": row['precio'],
                    "stock": row['stock'],
                    "marca": marca,
                    "proveedor": proveedor,
                    "categorias": categorias
                }
        except Exception as e:
            print(f"Error en get_by_id: {str(e)}")
            return None
        finally:
            cnx.close()

    def create(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO ARTICULOS 
                    (descripcion, precio, stock, marca_id, proveedor_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    self.descripcion,
                    self.precio,
                    self.stock,
                    self.marca.id if self.marca else None,
                    self.proveedor.id if self.proveedor else None
                ))
                articulo_id = cursor.lastrowid
                
                for categoria in self.categorias:
                    cursor.execute("""
                        INSERT INTO ARTICULOS_CATEGORIAS 
                        (articulo_id, categoria_id)
                        VALUES (%s, %s)
                    """, (articulo_id, categoria.id))
                
                cnx.commit()
                return articulo_id
        except Exception as e:
            cnx.rollback()
            print(f"Error en create: {str(e)}")
            return None
        finally:
            cnx.close()

    def update(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute("""
                    UPDATE ARTICULOS SET
                    descripcion = %s,
                    precio = %s,
                    stock = %s,
                    marca_id = %s,
                    proveedor_id = %s
                    WHERE id = %s
                """, (
                    self.descripcion,
                    self.precio,
                    self.stock,
                    self.marca.id if self.marca else None,
                    self.proveedor.id if self.proveedor else None,
                    self.id
                ))
                
                cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,))
                
                for categoria in self.categorias:
                    cursor.execute("""
                        INSERT INTO ARTICULOS_CATEGORIAS 
                        (articulo_id, categoria_id)
                        VALUES (%s, %s)
                    """, (self.id, categoria.id))
                
                cnx.commit()
                return True
        except Exception as e:
            cnx.rollback()
            print(f"Error en update: {str(e)}")
            return False
        finally:
            cnx.close()

    @staticmethod
    def delete(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
                cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
                cnx.commit()
                return True
        except Exception as e:
            cnx.rollback()
            print(f"Error en delete: {str(e)}")
            return False
        finally:
            cnx.close()