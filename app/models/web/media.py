from .. import db
from datetime import datetime, timezone
from app.utils.decorators import repr


class Media(db.Model):
    __tablename__ = 'web_media'
    media_id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    web_post_id = db.Column(db.Integer, db.ForeignKey('web_post.id'), nullable=True)
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    # Relationship
    web_post = db.relationship('Post', backref='medias')
    
    def __repr__(self):
        return repr(self)
    