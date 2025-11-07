from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, request, jsonify
from ..utils.repo import product_repo
from .forms import PostForm

from .. import db
from .models import Product
from sqlalchemy import select 

@post_bp.route('/products', methods=['GET']) 
def get_products():
    stmt = select(Product) 
    products = db.session.scalars(stmt).all()
    # Перетворюємо продукти у словники
    products_list = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        } 
        for product in products
        ]   
    return jsonify(products_list), 200
    #implement render_template replacing the line with jsonify
    #return render_template("products.html", products=products)

@post_bp.route('/products/<int:id>') 
def detail_post(id):
    if id > 10:
        abort(404)
    product = product_repo.get_by_id(id)
    return render_template("detail_post.html", 
                           product=product)

@post_bp.route('/products/new', methods=['GET', 'POST']) 
def create_product():    
    form = PostForm()
    if form.validate_on_submit():
        product_data = {
                "name": form.name.data,
                "content": form.content.data,
                "price": float(form.price.data)
        }
        product_repo.create(product_data)
        flash("Product created successfully!", "success")
        return redirect(url_for('.get_products'))
    if request.method == 'POST':
        flash("Error in form submission. Please check the fields.", "danger")    
    return render_template("create_product.html", form=form)