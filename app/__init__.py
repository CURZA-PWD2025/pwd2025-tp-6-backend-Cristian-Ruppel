from flask import Flask
from .articulos import articulo_bp
from .categorias import categoria_bp
from .marcas import marca_bp
from .proveedores import proveedor_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    app.register_blueprint(articulo_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    
    return app