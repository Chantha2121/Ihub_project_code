from flask import render_template, redirect, url_for, flash, request

from app.blueprints.web import web_bp

@web_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")