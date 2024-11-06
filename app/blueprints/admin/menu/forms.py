from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField, SubmitField
from wtforms.validators import DataRequired

class MenuForm(FlaskForm):
    hidden_id = HiddenField("ID")
    code = StringField("Code", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    icon = StringField("Icon Class", validators=[DataRequired()])
    order = IntegerField("Order", validators=[DataRequired()])
    submit = SubmitField("Submit")