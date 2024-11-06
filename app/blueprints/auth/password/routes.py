
from flask import render_template, request, Blueprint, url_for
from app.utils.global_vars import Message, Alert
from .forms import ChangePassForm
from app.models import User,db
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

password_bp = Blueprint("password_bp", __name__, url_prefix="/password", template_folder="templates")

@password_bp.route("/change_password", methods=['GET', 'POST'])
@login_required
def change_password():
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":"Change password","url":url_for(request.endpoint)}
    ]
    form = ChangePassForm()
    msg = []
    try:
        user = User.query.filter_by(id = current_user.id).first()
        if request.method == "POST" and form.validate_on_submit():
            old_pass = form.current_password.data
            if user and user.check_password(old_pass): 
                new_pass = form.new_password.data
                user.set_password(new_pass)
                db.session.commit()
                msg= Alert.alert_success()
            else:
                msg = Alert.alert_failed("Old password is not correct.")
        else:
            form.username.data = user.username
    except SQLAlchemyError as e:
        db.session.rollback()
        msg = Alert.alert_failed(f"Error: {e}")
        print(f"Error: {e}")
        
    return render_template('change_password.html', form = form, msg = msg,breadcrumb=breadcrumb)