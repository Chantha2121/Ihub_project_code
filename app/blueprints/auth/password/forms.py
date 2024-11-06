from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class ChangePassForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    confirm_password = PasswordField("Re-Password", validators=[DataRequired(),EqualTo('new_password')])
    submit = SubmitField("Reset Password")