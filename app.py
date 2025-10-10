from flask import Flask, request, redirect, url_for, render_template, abort
from utils.repo import product_repo

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route('/products') 
def get_products():
    products = product_repo.get_all()
    return render_template("products/products.html", 
                           products=products)

@app.route('/product/<int:id>') 
def detail_post(id):
    if id > 3:
        abort(404)
    product = product_repo.get_by_id(id)
    return render_template("products/detail_post.html", 
                           product=product)

@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    return "indesx page"


@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    user_agent = str(request.user_agent)[:10]
    return render_template("home.html", 
                           agent=user_agent)

@app.route('/hi/')
@app.route('/hi/<string:name>')  # /hi/ivan?age=30
def greetings(name=None):
    if  name is None:
        name = ""
    name = name.upper()
    age = request.args.get("age", 0, type=int)

    return render_template("hi.html", 
                           name=name,
                           age=age)



@app.route('/admin')
def admin():
    to_url = url_for("greetings", name="administrator", _external=True)    # --> "http://localhost:8080/hi/administrator"
    print(to_url)
    return redirect(to_url)

if __name__ == "__main__":
    app.run()  # Launch built-in web server and run this Flask webapp, debug=True
 

