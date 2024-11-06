from datetime import datetime, timezone
from .. import db
from app.utils.decorators import repr

class Post(db.Model):
    __tablename__ = 'web_post'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable = False)
    content = db.Column(db.Text, nullable = False)
    auth_user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'), nullable = False)
    web_category_id = db.Column(db.Integer, db.ForeignKey('web_category.id'), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    #Relationship
    auth_user = db.relationship("User", backref = "posts")
    web_category = db.relationship("Category", backref = "posts")

    def __repr__(self):
        return repr(self)