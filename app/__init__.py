from flask import Flask
from .config import config_map
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from flask_migrate import Migrate
import os

from dotenv import load_dotenv
load_dotenv()

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })


db = SQLAlchemy(model_class=Base)
migrate = Migrate()

# Функція створення застосунку фабричного типу
def create_app(config_name: str = os.environ.get("FLASK_CONFIG", "dev")) -> Flask:

    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    print(f"Running in config: {config_name}")


    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context(): 
        from .views import main as main_blueprint
        app.register_blueprint(main_blueprint)
        from .products import post_bp
        app.register_blueprint(post_bp, url_prefix="/shop")

        if config_name == "test":
            print("Registered routes:")
            for rule in app.url_map.iter_rules():
                print(rule)
     
    return app