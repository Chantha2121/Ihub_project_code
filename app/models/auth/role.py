from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr

class Role(db.Model):
    
    __tablename__ = 'auth_role'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60),unique = True, nullable =False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
 
    def __repr__(self):
        return repr(self)