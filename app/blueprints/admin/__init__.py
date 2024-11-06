from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__, url_prefix="/admin")
from app.blueprints.admin.menu import routes 

from .menu.routes import menu_bp
from .panel.routes import panel_bp

admin_bp.register_blueprint(menu_bp)
admin_bp.register_blueprint(panel_bp)
