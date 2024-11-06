from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import db
from app.utils.decorators import repr

class User(UserMixin, db.Model):
    __tablename__ = 'auth_user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    auth_role_id = db.Column(db.Integer, db.ForeignKey('auth_role.id'), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    #Relationship
    auth_role = db.relationship("Role", backref = "users")

    def __repr__(self):
        return repr(self)

    def set_password(self, password):
        """Hash the user's password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password, password)