import os

# A projekt gyökérkönyvtárának meghatározása
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_fallback_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    # Fejlesztői adatbázis: dev.db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'dev.db')

class ProductionConfig(Config):
    # Éles adatbázis: prod.db (vagy később PostgreSQL URL)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'prod.db')

# Szótár a config könnyű kiválasztásához
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}