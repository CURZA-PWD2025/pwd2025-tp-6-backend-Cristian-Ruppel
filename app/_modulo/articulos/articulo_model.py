from app._modulo.database.conect_db import ConectDB
from app._modulo.marcas.marca_model import MarcaModel
from app._modulo.proveedores.proveedor_model import ProveedorModel
from app._modulo.categorias.categoria_model import CategoriaModel

class ArticuloModel:
    def __init__(self, id=0, descripcion="", precio=0.0, stock=0, marca_id=None, proveedor_id=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id  
        self.proveedor_id = proveedor_id 
        self._marca = None  
        self._proveedor = None  
        self._categorias = []  

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca_id": self.marca_id,
            "proveedor_id": self.proveedor_id
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get('id'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            marca_id=data.get('marca_id'),
            proveedor_id=data.get('proveedor_id')
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, descripcion, precio, stock, marca_id, proveedor_id FROM ARTICULOS")
                articulos = []
                for row in cursor.fetchall():
                    articulo = ArticuloModel(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        precio=row['precio'],
                        stock=row['stock'],
                        marca_id=row['marca_id'],
                        proveedor_id=row['proveedor_id']
                    )
                    articulos.append(articulo)
                return articulos
        except Exception as e:
            print(f"Error en get_all: {str(e)}")
            return []
        finally:
            cnx.close()

    @staticmethod
    def get_by_id(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, descripcion, precio, stock, marca_id, proveedor_id FROM ARTICULOS WHERE id = %s", (id,))
                row = cursor.fetchone()
                if not row:
                    return None
                return ArticuloModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    stock=row['stock'],
                    marca_id=row['marca_id'],
                    proveedor_id=row['proveedor_id']
                )
        except Exception as e:
            print(f"Error en get_by_id: {str(e)}")
            return None
        finally:
            cnx.close()

    def cargar_marca(self):
        if self.marca_id and not self._marca:
            self._marca = MarcaModel.get_by_id(self.marca_id)
        return self._marca

    def cargar_proveedor(self):
        if self.proveedor_id and not self._proveedor:
            self._proveedor = ProveedorModel.get_by_id(self.proveedor_id)
        return self._proveedor

    def cargar_categorias(self):
        if not self._categorias and self.id:
            cnx = ConectDB.get_connect()
            try:
                with cnx.cursor(dictionary=True) as cursor:
                    cursor.execute(
                        "SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", 
                        (self.id,)
                    )
                    categorias_ids = [row['categoria_id'] for row in cursor.fetchall()]
                    self._categorias = [CategoriaModel.get_by_id(id) for id in categorias_ids]
            finally:
                cnx.close()
        return self._categorias

    def create(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return True
        except Exception as e:
            cnx.rollback()
            print(f"Error en create: {str(e)}")
            return False
        finally:
            cnx.close()

    def update(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "UPDATE ARTICULOS SET "
                    "descripcion = %s, precio = %s, stock = %s, "
                    "marca_id = %s, proveedor_id = %s "
                    "WHERE id = %s",
                    (self.descripcion, self.precio, self.stock,
                     self.marca_id, self.proveedor_id, self.id)
                )
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