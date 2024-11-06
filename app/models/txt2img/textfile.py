from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr

class TextFile(db.Model):
    
    __tablename__ = 'txt2img_textfile'
    
    id = db.Column(db.Integer, primary_key = True)
    textstyle_id = db.Column(db.Integer,db.ForeignKey('txt2img_textstyle.id'), nullable = False )
    code = db.Column(db.String(20), unique=True, nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    nb_record = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(200), nullable=True)
    download_url = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    #Relationship
    textstyle = db.relationship("TextStyle", backref = "textfiles")
    
    def __repr__(self):
        return repr(self)