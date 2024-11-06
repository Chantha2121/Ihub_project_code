from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class TextFileForm(FlaskForm):
    hidden_id = HiddenField("ID")
    textstyle_id = SelectField("Text Style", validators=[DataRequired()])
    code = StringField("Code", validators=[DataRequired()])
    filename = StringField("Filename", validators=[DataRequired()])
    nb_record = IntegerField("Nb Record(s)", validators=[DataRequired()])
    status = BooleanField("Status", validators=[DataRequired()])
    download_url = StringField("Url")
    submit = SubmitField("Submit")