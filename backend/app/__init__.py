from flask import Flask
from flask_cors import CORS
from .articulos.articulo_routes import articulo_bp
from .categorias.categoria_routes import categoria_bp
from .marcas.marca_routes import marca_bp
from .proveedores.proveedor_routes import proveedor_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
    
    app.register_blueprint(articulo_bp, url_prefix='/api')
    app.register_blueprint(categoria_bp, url_prefix='/api')
    app.register_blueprint(marca_bp, url_prefix='/api')
    app.register_blueprint(proveedor_bp, url_prefix='/api')
    
    return app