from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5000"], "methods": ["GET", "POST", "PUT", "DELETE"]}})

    # Configuraciones
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.secret_key = os.urandom(24)
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    
    # Inicializa las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

app = create_app()
app.app_context().push()