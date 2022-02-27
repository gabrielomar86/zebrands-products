from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from src.infrastructure.config.config import Config
from src.infrastructure.config.database import db

from .controllers.auth import auth
from .controllers.product import product
from .controllers.user import user

from src.infrastructure.config.login_manager import login_manager

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    
    login_manager.init_app(app)
    
    db.init_app(app)
    
    migrate = Migrate(app, db, directory='src/infrastructure/migrations')
    
    app.register_blueprint(auth)
    app.register_blueprint(product)
    app.register_blueprint(user)
    
    return app, db