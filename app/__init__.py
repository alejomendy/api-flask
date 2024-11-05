from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from flask_cors import CORS
# Crear instancias sin inicializar
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
   

    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.secret_key = os.urandom(24)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    # Importar rutas
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

# Crear la instancia de la aplicación
app = create_app()

# Asegurar que estamos en el contexto de la aplicación
app.app_context().push()