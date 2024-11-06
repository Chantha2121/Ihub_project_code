from flask import Flask
from app.utils.login import login_manager
from app.config import config
from app.models import db

# Import models here to register them
from app.models import *

def create_app():
    
    app = Flask(__name__)
    # Load flask configuration
    app.config.from_object(config['dev'])
    
    # Initialized flask Login Manager
    login_manager.init_app(app)
    
    # Initialize database and CSRF protection
    db.init_app(app)
    
    # Register blueprint
    from app.blueprints.api import api_bp
    app.register_blueprint(api_bp)
    
    from app.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.blueprints.web import web_bp
    app.register_blueprint(web_bp)
    
    from app.blueprints.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    from app.blueprints.apps import apps_bp
    app.register_blueprint(apps_bp)
    
    
    return app