from flask import render_template, Blueprint, url_for, request
from app.utils.global_vars import Message, Alert
from app.models import db, TextFile, TextStyle
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from .forms import TextFileForm

txt2img_bp = Blueprint("txt2img_bp", __name__, url_prefix="/txt2img", template_folder="templates")

@txt2img_bp.route('/index')
@login_required
def index():
    title = "Text to Image"
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":title,"url":url_for(request.endpoint)}
    ]
    msg = []
    data = db.session.query(TextFile, TextStyle) \
                   .join(TextStyle, TextFile.textstyle_id == TextStyle.id) \
                   .with_entities(TextFile.id, TextFile.code, TextStyle.name, TextFile.filename \
                       , TextFile.nb_record, TextFile.status, TextFile.download_url ) \
                   .all()
    
    return render_template("txt2img_index.html",data = data,title=title, msg=msg, breadcrumb=breadcrumb)

@txt2img_bp.route("/create", methods=["GET","POST"])
def create():
    title = "New Text File"
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":title,"url":url_for(request.endpoint, id=0)}
    ]
    msg = []
    frm = TextFileForm()
    frm.textstyle_id.choices = [('', 'Select')] + [(obj.id, obj.name) for obj in TextStyle.query.all()]
    if request.method=="POST" and frm.validate_on_submit():
        try:
            new_record = TextFile(
                textstyle_id = frm.textstyle_id.data,
                code = frm.code.data,
                filename = frm.code.data,
                nb_record = 0,
                status = False
            )
            db.session.add(new_record)
            db.session.commit()
            
        except SQLAlchemyError as e:
            db.session.rollback()
            msg = Alert.alert_failed(f"Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            msg = Alert.alert_failed(f"Error: {e}")
            
    render_template('txt2img_create.html', frm = frm, title=title,breadcrumb=breadcrumb, msg = msg)
    
@txt2img_bp.route('/form/<int:id>', methods=["GET", "POSt"])
@login_required
def form(id):
    title = "New Main Menu"
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":title,"url":url_for(request.endpoint, id=0)}
    ]
    msg = []
    form = TextFileForm()

    #Assign value only firs time
    if not form.hidden_id.data:
        form.hidden_id.data = id
        
    if request.method == "GET" and form.hidden_id.data != 0:
        title = "Update Main Menu"
        tbl = TextFile.query.filter_by(id=int(form.hidden_id.data)).first()
        textfile = TextFile.query.get_or_404(id)
        form = TextFileForm(obj=textfile)
        if textfile is None:
            msg = Alert.alert_failed("Record not found.")
            
    elif request.method == "POST":
        if int(form.hidden_id.data)==0 and form.validate_on_submit():
            try:
                tbl = TextFile()
                tbl.textstyle_id = form.textstyle_id.data
                tbl.code = form.code.data
                tbl.filename = form.file_name.data
                tbl.nb_record = 0
                tbl.status = False
                db.session.add(tbl)
                db.session.commit()
                
                form.hidden_id.data = tbl.id
                msg = Alert.alert_success()
                title = "Update Main Menu"
                
            except SQLAlchemyError as e:
                db.session.rollback()
                msg = Alert.alert_failed(f"Error: {e}")
                print(f"Error: {e}")
            except Exception as e:
                msg = Alert.alert_failed(f"Error: {e}")
        elif int(form.hidden_id.data)>0 and form.validate_on_submit():
            tbl = Menu.query.filter_by(id=int(form.hidden_id.data)).first()
            if tbl:
                tbl.code = form.code.data
                tbl.name = form.name.data
                tbl.icon = form.icon.data
                tbl.order = form.order.data
                try:
                    db.session.commit()
                    
                    form.hidden_id.data = tbl.id
                    msg = Alert.alert_success()
                    title = "Update Main Menu"
                except Exception as e:
                    db.session.rollback()
                    msg = Alert.alert_failed(f"Error: {e}")
            else:
                msg = Alert.alert_failed("Record not found.")
    return render_template('menu_form.html', form = form, title=title,breadcrumb=breadcrumb, msg = msg)