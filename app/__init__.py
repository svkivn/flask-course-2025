from flask import Flask
from .config import config_map
from .extensions import init_extensions, db
import os

from dotenv import load_dotenv
load_dotenv()


def register_blueprints(app: Flask):
    """Реєструє всі блюпринти в одному місці"""
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .products import post_bp
    app.register_blueprint(post_bp, url_prefix="/shop")


# Функція створення застосунку фабричного типу
def create_app(config_name: str = os.environ.get("FLASK_CONFIG", "dev")) -> Flask:

    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    print(f"Running in config: {config_name} with {app.root_path=}")

    init_extensions(app)

    with app.app_context(): 
        register_blueprints(app)
         
    return app