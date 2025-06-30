from app.database.conect_db import ConectDB

class CategoriaModel:
    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return CategoriaModel(
            id=int(data.get('id', 0)),
            nombre=data.get('nombre', '').strip()
        )

    @staticmethod
    def get_all():
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM categorias")
                return [CategoriaModel.deserializar(row) for row in cursor.fetchall()]

    @staticmethod
    def get_one(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
                if result := cursor.fetchone():
                    return CategoriaModel.deserializar(result)

    def create(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO categorias (nombre) VALUES (%s)",
                    (self.nombre,)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return True

    def update(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "UPDATE categorias SET nombre=%s WHERE id=%s",
                    (self.nombre, self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0

    @staticmethod
    def delete(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute("DELETE FROM categorias WHERE id=%s", (id,))
                cnx.commit()
                return cursor.rowcount > 0