import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))  

class ConectDB:
    @staticmethod
    def get_connect():
        try:
            return mysql.connector.connect(
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', ''),
                host=os.getenv('DB_HOST', '127.0.0.1'),
                port=os.getenv('DB_PORT', '3308'),
                database=os.getenv('DB_NAME', 'pwd2025_tp6'),
                auth_plugin='mysql_native_password'
            )
        except Exception as ex:
            raise ConnectionError(
                f"Error de conexión a DB. Verifica:\n"
                f"1. XAMPP con MySQL activo\n"
                f"2. Puerto 3308 disponible\n"
                f"3. Variables en .env\n"
                f"Detalle: {str(ex)}"
            )

    @staticmethod
    def execute_query(sql, params=None, fetch=False):
        conn = None
        try:
            conn = ConectDB.get_connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, params or ())
            conn.commit()
            return cursor.fetchall() if fetch else cursor.rowcount
        except Exception as ex:
            if conn:
                conn.rollback()
            raise
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()