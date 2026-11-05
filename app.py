from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Application configuration
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)
migrate = Migrate(app, db)

# Model
class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False
    )

    # price: Mapped[float] = mapped_column(
    #     db.Float,
    #     nullable=False
    # )

    def __repr__(self):
        return f"<Product {self.name}: {self.price}>"


# # CREATE TABLE
# with app.app_context():
#     db.create_all()
#     #db.drop_all()


# CREATE: add products
@app.route("/products/create")
def create_products():

    products = [
        Product(name="Keyboard", price=49.99),
        Product(name="Mouse", price=24.50)
    ]

    db.session.add_all(products)
    db.session.commit()

    return "Products added successfully!"


# READ: retrieve all products
@app.route("/products")
def get_products():

    stmt = db.select(Product).order_by(Product.id)

    products = db.session.execute(stmt).scalars().all()

    result = "<h2>All products</h2>"

    for product in products:
        result += (
            f"<p>ID: {product.id}, "
            f"Name: {product.name}, "
            f"Price: {product.price}</p>"
        )

    return result


# READ: retrieve one product by ID
@app.route("/products/<int:product_id>")
def get_product(product_id):

    product = db.get_or_404(Product, product_id)

    return (
        f"ID: {product.id}, "
        f"Name: {product.name}, "
        f"Price: {product.price}"
    )


# UPDATE: modify product price
@app.route("/products/update")
def update_product():

    stmt = db.select(Product).where(
        Product.name == "Keyboard"
    )

    product = db.session.execute(stmt).scalar_one_or_none()

    if product is None:
        return "Product not found", 404

    product.price = 39.99

    db.session.commit()

    return f"New price: {product.price}"


# DELETE: delete product by ID
@app.route(
    "/products/<int:product_id>/delete",
    methods=["POST"]
)
def delete_product(product_id):

    product = db.get_or_404(Product, product_id)

    db.session.delete(product)
    db.session.commit()

    return f"Deleted product {product_id}"


# Run application
if __name__ == "__main__":
    app.run(debug=True)



#https://www.deployhq.com/blog/mastering-code-first-database-deployments-with-flask-and-sqlalchemy