from app.database.conect_db import ConectDB

class MarcaModel:
    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return MarcaModel(
            id=int(data.get('id', 0)),
            nombre=data.get('nombre', '').strip()
        )

    @staticmethod
    def get_all():
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM marcas")
                return [MarcaModel.deserializar(row) for row in cursor.fetchall()]

    @staticmethod
    def get_one(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM marcas WHERE id = %s", (id,))
                if result := cursor.fetchone():
                    return MarcaModel.deserializar(result)

    def create(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO marcas (nombre) VALUES (%s)",
                    (self.nombre,)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return True

    def update(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "UPDATE marcas SET nombre = %s WHERE id = %s",
                    (self.nombre, self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0

    @staticmethod
    def delete(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute("DELETE FROM marcas WHERE id = %s", (id,))
                cnx.commit()
                return cursor.rowcount > 0