from flask import Blueprint

web_bp = Blueprint('web_bp', __name__, template_folder="templates")

from app.blueprints.web import routes