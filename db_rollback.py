import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def drop_tables():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()

    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("DROP TABLE IF EXISTS articulo_categoria")
    cursor.execute("DROP TABLE IF EXISTS articulos")
    cursor.execute("DROP TABLE IF EXISTS proveedores")
    cursor.execute("DROP TABLE IF EXISTS categorias")
    cursor.execute("DROP TABLE IF EXISTS marcas")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_tables()