from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix="/api")
#from app.blueprints.api import routes