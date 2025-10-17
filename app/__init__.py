from flask import Flask


app = Flask(__name__)
app.secret_key = "secret_key_12345"

from . import views

from .products import post_bp
app.register_blueprint(post_bp, url_prefix="/shop")