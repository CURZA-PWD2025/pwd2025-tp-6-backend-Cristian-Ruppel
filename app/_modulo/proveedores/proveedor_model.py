from app._modulo.database.conect_db import ConectDB

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
            id=data.get('id', 0),
            nombre=data.get('nombre', ""),
            telefono=data.get('telefono', ""),
            direccion=data.get('direccion', ""),
            email=data.get('email', "")
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES")
                return [ProveedorModel(**row).serializar() for row in cursor.fetchall()]
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
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
                result = cursor.fetchone()
                return ProveedorModel(**result).serializar() if result else None
        except Exception as e:
            print(f"Error en get_by_id: {str(e)}")
            return None
        finally:
            cnx.close()

    def create(self):
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)",
                    (self.nombre, self.telefono, self.direccion, self.email)
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
                    "UPDATE PROVEEDORES SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s",
                    (self.nombre, self.telefono, self.direccion, self.email, self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0
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
                cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
                cnx.commit()
                return True
        except Exception as e:
            cnx.rollback()
            print(f"Error en delete: {str(e)}")
            return False
        finally:
            cnx.close()