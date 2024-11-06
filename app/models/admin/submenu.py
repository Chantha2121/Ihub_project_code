from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr

class SubMenu(db.Model):
    
    __tablename__ = 'admin_submenu'
    
    id = db.Column(db.Integer, primary_key = True)
    admin_menu_id = db.Column(db.Integer,db.ForeignKey('admin_menu.id'), nullable = False )
    code = db.Column(db.String(50),unique = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    icon = db.Column(db.String(100), nullable = False)
    end_point = db.Column(db.String(200), nullable = False)
    order = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    #Relationship
    admin_menu = db.relationship("Menu", backref = "submenus")
    
    def __repr__(self):
        return f"<SubMenu {self.name}>"