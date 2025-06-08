from app.database.conect_db import ConectDB

class CategoriaModel:
    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            id=data.get('id', 0),
            nombre=data.get('nombre', "")
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, nombre FROM categorias")
                return [CategoriaModel(**row).serializar() for row in cursor.fetchall()]
        finally:
            cnx.close()

    @staticmethod
    def get_one(id):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, nombre FROM categorias WHERE id = %s", (id,))
                result = cursor.fetchone()
                return CategoriaModel(**result).serializar() if result else None
        finally:
            cnx.close()

    def create(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO categorias (nombre) VALUES (%s)",
                    (self.nombre,)
                )
                self.id = cursor.lastrowid
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
                cursor.execute(
                    "UPDATE categorias SET nombre = %s WHERE id = %s",
                    (self.nombre, self.id)
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
                cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
                cnx.commit()
                return True
        except Exception:
            cnx.rollback()
            return False
        finally:
            cnx.close()