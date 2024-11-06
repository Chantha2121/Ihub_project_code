from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr

class Menu(db.Model):
    
    __tablename__ = 'admin_menu'
    
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(50),unique = True, nullable=False)
    name = db.Column(db.String(100),unique = True, nullable =False)
    icon = db.Column(db.String(100), nullable = False)
    order = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
 
    def __repr__(self):
        return f"<Menu {self.name}>"