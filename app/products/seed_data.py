# seed_tech_data.py

from app import create_app, db
from app.products.models import Product, Category

app = create_app(config_name="dev")

with app.app_context():
    # --- Створюємо категорії ---
    laptops = Category(name="Laptops")
    smartphones = Category(name="Smartphones")
    tablets = Category(name="Tablets")

    db.session.add_all([laptops, smartphones, tablets])
    db.session.commit()

    # --- Створюємо продукти ---
    product1 = Product(
        name="Gaming Laptop", 
        price=1500.00, 
        active=False,
        category=laptops 
    )
    product2 = Product(
        name="Ultrabook", 
        price=1200.00, 
        active=True,
        category_id=laptops.id 
    )
    product3 = Product(
        name="iPhone 11", 
        price=403.99, 
        active=True,
        category=smartphones 
    )
    product4 = Product(
        name="Galaxy Tab S9", 
        price=750.00, 
        active=False
    )
    product5 = Product(
        name="USB-C Hub", 
        price=49.99, 
        active=True
    )  # без категорії

    product4.category = tablets  # Призначаємо категорію пізніше

    db.session.add_all([product1, product2, product3, product4, product5])
    db.session.commit()

    print("Database seeded with tech products, categories, prices, and active status.")
