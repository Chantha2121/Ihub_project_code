from flask import render_template, redirect, url_for, flash, request

from app.blueprints.api import api_bp

@api_bp.route('/api', methods=['GET', 'POST'])
def api():
    return "API"
