from app.database.conect_db import ConectDB

class ProveedorModel:
    def __init__(self, id=0, nombre="", telefono="", direccion="", email=""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=int(data.get('id', 0)),
            nombre=data.get('nombre', '').strip(),
            telefono=data.get('telefono', '').strip(),
            direccion=data.get('direccion', '').strip(),
            email=data.get('email', '').strip()
        )

    @staticmethod
    def get_all():
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM proveedores")
                return [ProveedorModel.deserializar(row) for row in cursor.fetchall()]

    @staticmethod
    def get_one(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id,))
                if result := cursor.fetchone():
                    return ProveedorModel.deserializar(result)

    def create(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO proveedores (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
                    (self.nombre, self.telefono, self.direccion, self.email)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return True

    def update(self):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "UPDATE proveedores SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s",
                    (self.nombre, self.telefono, self.direccion, self.email, self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0

    @staticmethod
    def delete(id):
        with ConectDB.get_connect() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute("DELETE FROM proveedores WHERE id=%s", (id,))
                cnx.commit()
                return cursor.rowcount > 0