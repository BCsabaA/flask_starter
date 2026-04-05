from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from .admin_utils import MyAdminIndexView

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
admin = Admin(
    name='Flask Starter Admin', 
    index_view=MyAdminIndexView(), 
    template_mode='bootstrap4')