from ...database.conect_db import ConectDB

class MarcaModel:
    def __init__(self, id=0, descripcion=""):
        self.id = id
        self.descripcion = descripcion

    def serialize(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return MarcaModel(
            id=data.get("id", 0),
            descripcion=data.get("descripcion", "")
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM marcas")
                return [MarcaModel(**row).serialize() for row in cursor.fetchall()]
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
                cursor.execute("SELECT * FROM marcas WHERE id = %s", (id,))
                result = cursor.fetchone()
                return MarcaModel(**result) if result else None
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
                    "INSERT INTO marcas (descripcion) VALUES (%s)",
                    (self.descripcion,)
                )
                cnx.commit()
                return cursor.lastrowid
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
                cursor.execute(
                    "UPDATE marcas SET descripcion = %s WHERE id = %s",
                    (self.descripcion, self.id)
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
                cursor.execute("DELETE FROM marcas WHERE id = %s", (id,))
                affected = cursor.rowcount
                cnx.commit()
                return affected > 0
        except Exception as e:
            cnx.rollback()
            print(f"Error en delete: {str(e)}")
            return False
        finally:
            cnx.close()