import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from .extensions import db, login_manager, migrate, admin
from .config import config_dict

def create_app():
    app = Flask(__name__)
    env = os.environ.get('APP_ENV', 'development')
    app.config.from_object(config_dict[env])
    
    # Kiegészítők inicializálása
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    
    # --- LOGGING BEÁLLÍTÁSA ---
    if not app.debug: # Éles módban fájlba naplózunk
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/flask_app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('Flask Starter indítása')

    # --- ADMIN FELÜLET ÉS MODELLEK ---
    from .models import User
    from flask_admin.contrib.sqla import ModelView
    
    # Alapértelmezett nézet a User táblához
    admin.add_view(ModelView(User, db.session))

    # --- FLASK-LOGIN USER LOADER (EZ HIÁNYZOTT!) ---
    @login_manager.user_loader
    def load_user(user_id):
        # SQLAlchemy 3.x esetén ez a modern, ajánlott szintaxis a lekérdezésre
        return db.session.get(User, int(user_id))

    # Blueprintek regisztrálása
    from .main import main_bp
    from .auth import auth_bp
    from .blog import blog_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app