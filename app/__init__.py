from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_map
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
import os

from dotenv import load_dotenv
load_dotenv()

class Base(DeclarativeBase):
    pass

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