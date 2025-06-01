from app._modulo.database.conect_db import ConectDB

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
            id=data.get('id'),
            nombre=data.get('nombre')  
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        try:
            with cnx.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, nombre FROM CATEGORIAS")  
                return [CategoriaModel(**row).serializar() for row in cursor.fetchall()]
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
                cursor.execute("SELECT id, nombre FROM CATEGORIAS WHERE id = %s", (id,))
                result = cursor.fetchone()
                return CategoriaModel(**result).serializar() if result else None
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
                    "INSERT INTO CATEGORIAS (nombre) VALUES (%s)", 
                    (self.nombre,)
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
                    "UPDATE CATEGORIAS SET nombre = %s WHERE id = %s", 
                    (self.nombre, self.id)
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
                cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE categoria_id = %s", (id,))
                cursor.execute("DELETE FROM CATEGORIAS WHERE id = %s", (id,))
                cnx.commit()
                return True
        except Exception as e:
            cnx.rollback()
            print(f"Error en delete: {str(e)}")
            return False
        finally:
            cnx.close()