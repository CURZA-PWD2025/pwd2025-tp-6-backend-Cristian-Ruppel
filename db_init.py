import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def create_database():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
    conn.close()

def run_migrations():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marcas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    ) ENGINE=InnoDB
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    ) ENGINE=InnoDB
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(20),
        direccion TEXT,
        email VARCHAR(100)
    ) ENGINE=InnoDB
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articulos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descripcion VARCHAR(255) NOT NULL,
        precio DECIMAL(10,2) NOT NULL,
        stock INT NOT NULL,
        marca_id INT NOT NULL,
        proveedor_id INT NOT NULL,
        FOREIGN KEY (marca_id) REFERENCES marcas(id),
        FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
    ) ENGINE=InnoDB
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articulo_categoria (
        articulo_id INT NOT NULL,
        categoria_id INT NOT NULL,
        PRIMARY KEY (articulo_id, categoria_id),
        FOREIGN KEY (articulo_id) REFERENCES articulos(id) ON DELETE CASCADE,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
    ) ENGINE=InnoDB
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    run_migrations()