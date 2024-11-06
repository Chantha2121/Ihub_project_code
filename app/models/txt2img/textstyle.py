from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr

class TextStyle(db.Model):
    
    __tablename__ = 'txt2img_textstyle'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    font_name = db.Column(db.String(200), nullable=False)
    font_size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
 
    def __repr__(self):
        return repr(self)