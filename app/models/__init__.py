from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .admin.menu import Menu
from .admin.submenu import SubMenu

from .auth.role import Role
from .auth.user import User

from .web.category import Category
from .web.media import Media
from .web.post import Post

from .txt2img.textfile import TextFile
from .txt2img.textstyle import TextStyle