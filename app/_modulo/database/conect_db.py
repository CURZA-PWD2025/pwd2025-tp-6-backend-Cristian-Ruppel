import mysql.connector

class ConectDB:
    @staticmethod
    def get_connect():
        try:
            return mysql.connector.connect(
                user="root",
                password="",
                host="localhost",
                port=3308,  
                database="pwd2025_tp6",
                auth_plugin='mysql_native_password'  
            )
        except Exception as ex:
            print(f"❌ Error de conexión: Verifica:\n1. XAMPP corriendo\n2. MySQL en puerto 3308\n3. Las tablas existen\nError técnico: {ex}")
            raise

    @staticmethod
    def execute_query(sql, params=None, fetch=False):
        conn = ConectDB.get_connect()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(sql, params or ())
            conn.commit()
            return cursor.fetchall() if fetch else cursor.rowcount
        finally:
            cursor.close()
            conn.close()