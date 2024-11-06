from flask import render_template, redirect, url_for, flash, Blueprint
from .forms import LoginForm
from app.models import User
from flask_login import login_user, login_required, logout_user, current_user


login_bp = Blueprint('login_bp', __name__, url_prefix="/login", template_folder="templates")


@login_bp.route('/index', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_bp.panel_bp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username = username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('admin_bp.panel_bp.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('auth_login.html', form = form)

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'primary')
    return redirect(url_for('auth_bp.login_bp.login'))