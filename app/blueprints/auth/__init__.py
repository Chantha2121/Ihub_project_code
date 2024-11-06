from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__, url_prefix="/auth")

from .login.routes import login_bp
from .password.routes import password_bp

auth_bp.register_blueprint(login_bp)
auth_bp.register_blueprint(password_bp)