from . import post_bp
from flask import render_template, abort
from ..utils.repo import product_repo

@post_bp.route('/products') 
def get_products():
    products = product_repo.get_all()
    return render_template("products.html", 
                           products=products)

@post_bp.route('/product/<int:id>') 
def detail_post(id):
    if id > 3:
        abort(404)
    product = product_repo.get_by_id(id)
    return render_template("detail_post.html", 
                           product=product)