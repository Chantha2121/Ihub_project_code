
from flask import render_template, Blueprint
from app.utils.global_vars import Message
from app.models import db, User,Menu, SubMenu
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


panel_bp = Blueprint("panel_bp", __name__, url_prefix="/panel", template_folder="templates")

@panel_bp.route("/index", methods=['GET', 'POST'])
@login_required
def index():
    mm = load_menu()
    return render_template("panel_index.html", mm = mm)

@panel_bp.route("/mm")
def load_menu():
    # Query to get all menus and their submenus, ordered by 'order'
    query = db.session.query(Menu).options(joinedload(Menu.submenus)).order_by(Menu.order.asc())
    
    menus = query.all()
    
    # Transform the results into the desired dictionary format
    menu_dict = []
    for menu in menus:
        menu_dict.append(
            {
                'id': menu.id,
                'code': menu.code,
                'name': menu.name,
                'icon': menu.icon,
                'order': menu.order,
                'submenus': [
                    {
                        'id': submenu.id,
                        'code': submenu.code,
                        'name': submenu.name,
                        'icon': submenu.icon,
                        'end_point': submenu.end_point,
                        'order': submenu.order
                    }
                    # Sorting the submenus by 'order' field in ascending order
                    for submenu in sorted(menu.submenus, key=lambda x: x.order)
                ]
            }
        )

    # Output the dictionary
    menu_dict
    print(str(query))
    return menu_dict

@panel_bp.route("/homepage")
@login_required
def homepage():
    return render_template("panel_homepage.html")