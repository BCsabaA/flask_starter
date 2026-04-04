import os
from flask import Flask
from dotenv import load_dotenv

from .extensions import db, login_manager
from .config import config_dict

def create_app():
    # .env fájl betöltése
    load_dotenv()
    
    app = Flask(__name__)
    
    # Környezet kiválasztása (alapértelmezett: development)
    env = os.environ.get('APP_ENV', 'development')
    app.config.from_object(config_dict[env])
    
    # Kiegészítők inicializálása az app-pal
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # Ide irányít, ha védett oldalra mész bejelentkezés nélkül
    login_manager.login_message = "Kérlek jelentkezz be az oldal megtekintéséhez."
    login_manager.login_message_category = "warning"
    
    # Modellek importálása (hogy az SQLAlchemy lássa őket a táblageneráláskor)
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Adatbázis táblák létrehozása, ha nem léteznek
    with app.app_context():
        db.create_all()

    # Blueprintek (modulok) regisztrálása
    from .main import main_bp
    from .auth import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app