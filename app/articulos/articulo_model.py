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
        self.marca = marca if marca else {}
        self.proveedor = proveedor if proveedor else {}
        self.categorias = categorias if categorias else []

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca,
            "proveedor": self.proveedor,
            "categorias": self.categorias
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get('id', 0),
            descripcion=data.get('descripcion', ""),
            precio=data.get('precio', 0.0),
            stock=data.get('stock', 0),
            marca=data.get('marca', {}),
            proveedor=data.get('proveedor', {}),
            categorias=data.get('categorias', [])
        )

    @staticmethod
    def get_one(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM articulos WHERE id = %s", (id,))
                row = cursor.fetchone()
                if not row:
                    return None

                marca = MarcaModel.get_one(row['marca_id'])
                proveedor = ProveedorModel.get_one(row['proveedor_id'])
                categorias = ArticuloModel._get_categorias_by_articulo_id(row['id'])

                articulo = ArticuloModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    stock=row['stock'],
                    marca=marca,
                    proveedor=proveedor,
                    categorias=categorias
                )
                return articulo.serializar()
        finally:
            cnx.close()

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM articulos")
                rows = cursor.fetchall()
                articulos = []
                for row in rows:
                    marca = MarcaModel.get_one(row['marca_id'])
                    proveedor = ProveedorModel.get_one(row['proveedor_id'])
                    categorias = ArticuloModel._get_categorias_by_articulo_id(row['id'])
                    articulo = ArticuloModel(
                        id=row['id'],
                        descripcion=row['descripcion'],
                        precio=row['precio'],
                        stock=row['stock'],
                        marca=marca,
                        proveedor=proveedor,
                        categorias=categorias
                    )
                    articulos.append(articulo.serializar())
                return articulos
        finally:
            cnx.close()

    @staticmethod
    def _get_categorias_by_articulo_id(articulo_id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                query = """
                    SELECT c.id, c.nombre 
                    FROM categorias c
                    JOIN articulo_categoria ac ON c.id = ac.categoria_id
                    WHERE ac.articulo_id = %s
                """
                cursor.execute(query, (articulo_id,))
                return cursor.fetchall()
        finally:
            cnx.close()

    def create(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                marca_id = self.marca.get('id') if self.marca and self.marca.get('id') else None
                proveedor_id = self.proveedor.get('id') if self.proveedor and self.proveedor.get('id') else None

                cursor.execute(
                    "INSERT INTO articulos (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
                    (self.descripcion, self.precio, self.stock, marca_id, proveedor_id)
                )
                self.id = cursor.lastrowid

                if self.categorias:
                    for cat in self.categorias:
                        cursor.execute(
                            "INSERT INTO articulo_categoria (articulo_id, categoria_id) VALUES (%s, %s)",
                            (self.id, cat.get('id'))
                        )

                cnx.commit()
                return True
        except Exception:
            cnx.rollback()
            return False
        finally:
            cnx.close()

    def update(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                marca_id = self.marca.get('id') if self.marca and self.marca.get('id') else None
                proveedor_id = self.proveedor.get('id') if self.proveedor and self.proveedor.get('id') else None

                cursor.execute(
                    "UPDATE articulos SET descripcion = %s, precio = %s, stock = %s, marca_id = %s, proveedor_id = %s WHERE id = %s",
                    (self.descripcion, self.precio, self.stock, marca_id, proveedor_id, self.id)
                )

                cursor.execute("DELETE FROM articulo_categoria WHERE articulo_id = %s", (self.id,))
                if self.categorias:
                    for cat in self.categorias:
                        cursor.execute(
                            "INSERT INTO articulo_categoria (articulo_id, categoria_id) VALUES (%s, %s)",
                            (self.id, cat.get('id'))
                        )

                cnx.commit()
                return cursor.rowcount > 0
        except Exception:
            cnx.rollback()
            return False
        finally:
            cnx.close()

    @staticmethod
    def delete(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute("DELETE FROM articulo_categoria WHERE articulo_id = %s", (id,))
                cursor.execute("DELETE FROM articulos WHERE id = %s", (id,))
                cnx.commit()
                return True
        except Exception:
            cnx.rollback()
            return False
        finally:
            cnx.close()
