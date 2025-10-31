import os
from dotenv import load_dotenv

load_dotenv()  # завантажує змінні з .env
#print("Keys from .env:", os.environ.get("SECRET_KEY"), os.environ.get("DEV_DATABASE_URL"))

# Визначення базового каталогу - абсолютний шлях до папки, де знаходиться config.py
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_DEBUG = 1 # для автоматичного перезавантаження
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "data.db")
    )


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_map = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}
