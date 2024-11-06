from flask import Blueprint

apps_bp = Blueprint('apps_bp', __name__, url_prefix="/apps")

from .txt2img.routes import txt2img_bp

apps_bp.register_blueprint(txt2img_bp)