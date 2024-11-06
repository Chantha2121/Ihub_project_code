from flask import render_template, Blueprint, url_for, request
from app.utils.global_vars import Message, Alert
from app.models import db, Menu
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from .forms import MenuForm

menu_bp = Blueprint("menu_bp", __name__, url_prefix="/menu", template_folder="templates")

@menu_bp.route('/index')
@login_required
def index():
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":"Main Menu","url":url_for(request.endpoint)}
    ]
    msg = []
    data  = db.session.query(Menu).with_entities(Menu.id,Menu.code, Menu.name, Menu.icon, Menu.order).all()
    
    return render_template("menu_index.html",data = data, msg=msg, breadcrumb=breadcrumb)

@menu_bp.route('/form/<int:id>', methods=["GET", "POSt"])
@login_required
def form(id):
    title = "New Main Menu"
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":title,"url":url_for(request.endpoint, id=0)}
    ]
    
    msg = []
    form = MenuForm()

    #Assign value only firs time
    if not form.hidden_id.data:
        form.hidden_id.data = id
        
    if request.method == "GET" and form.hidden_id.data != 0:
        title = "Update Main Menu"
        tbl = Menu.query.filter_by(id=int(form.hidden_id.data)).first()
        if tbl:
            form.code.data = tbl.code
            form.name.data = tbl.name
            form.icon.data = tbl.icon
            form.order.data = tbl.order
        else:
            msg = Alert.alert_failed("Record not found.")
    elif request.method == "POST":
        if int(form.hidden_id.data)==0 and form.validate_on_submit():
            try:
                tbl = Menu()
                tbl.code = form.code.data
                tbl.name = form.name.data
                tbl.icon = form.icon.data
                tbl.order = form.order.data
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

@menu_bp.route('/detail/<int:id>', methods=["GET", "POSt"])
@login_required
def detail(id):
    breadcrumb = [
        {"label":"Home", "url": "#"},
        {"label":"Main Menu Detail","url":url_for(request.endpoint, id=id)}
    ]
    title = "Main Menu Detail"
    msg = []
    form = MenuForm()
    form.submit.label.text = "Delete"
    form.hidden_id.data=id
    if request.method == "GET" and form.hidden_id.data != 0:
        tbl = Menu.query.filter_by(id=int(form.hidden_id.data)).first()
        if tbl:
            form.code.data = tbl.code
            form.name.data = tbl.name
            form.icon.data = tbl.icon
            form.order.data = tbl.order
        else:
            msg = Alert.alert_failed("Record not found.")
    elif request.method == "POST" and form.validate_on_submit():
        tbl = Menu.query.filter_by(id=int(form.hidden_id.data)).first()
        if tbl:
            try:
                db.session.delete(tbl)
                db.session.commit()
                msg = Alert.alert_success()
            except Exception as e:
                db.session.rollback()
                msg = Alert.alert_failed(f"Error: {e}")
        else:
            msg = Alert.alert_failed("Record not found.")

    return render_template('menu_detail.html', form = form, title = title, msg = msg,breadcrumb=breadcrumb)