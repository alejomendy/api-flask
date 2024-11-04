from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
   
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.urandom(24)
    db.init_app(app)
    migrate.init_app(app, db)

    
        
        
    from .routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
