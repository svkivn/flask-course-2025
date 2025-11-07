# Flask Course 2025 — Lesson: SQLa

# Product Blueprint — Models and Routes

Overview
- A small, well-structured Flask blueprint that exposes CRUD for a Product.

Recommendations:

- Use the new SQLAlchemy 2.0 style with with Flask-SQLAlchemy and db.Model. Prefer Mapped and mapped_column instead of the old db.Column. Use proper Python types (int, str, Decimal) for autocomplete and static type checking.
Establish bidirectional relationships and ForeignKey

- Migrations. Use Flask-Migrate (Alembic) to manage database schema changes. Use migration scripts when changing column types or relationships.

- Control loading strategy (lazy) and avoid N+1 queries. 
Choose lazy="select", lazy="joined", or lazy="dynamic" depending on usage.
Use joinedload or selectinload when querying lists to prevent excessive queries.

Recommended file layout
- app/
    - products/
        - __init__.py         # defines product_bp (Blueprint) and registers routes
        - models.py           # SQLAlchemy models: Product
        - views.py            # route handlers using product_bp
        - forms.py
- migrations/                 # Flask-Migrate migrations

Models (SQLAlchemy)
- Product
    - id: Integer, primary key
    - name: String, required, indexed
    - price: Numeric/Decimal(precision), required, default 0.00
    - active: Boolean, default True
    - category_id: ForeignKey -> Category.id, nullable
    - created_at, updated_at: DateTime (auto-managed)
    - relationship: category (many products → one category)

- Category
    - id: Integer, primary key
    - name: String, required, unique
    - slug: String, indexed, unique
    - relationship: products (backref)

Example models.py (concise)
```python
from datetime import datetime
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, Numeric, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    slug: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)

    # Зв'язок з продуктами (один до багатьох)
    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
        lazy="select"  # або 'dynamic' / 'joined'
    )

class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # ForeignKey + двосторонній зв'язок
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category" | None] = relationship("Category", back_populates="products")
```


Recommendations for Flask Blueprint:
 -Use lazy="select" for simple or small datasets. (list of obj)
- Use lazy="joined" for list views to avoid N+1 queries. (list of json)
- Use lazy="dynamic" for large product lists when filtering or paginating. (query)


Blueprint routes (views)
- URL prefix: /products
- Endpoints:
    - GET /products
        - list products, support query params
        - support query params
    - GET /products/<int:id>
        - return single product or 404
    - GET/POST /products/create
        - create new product 
    - GET/POST /products/<int:id>/updated
        - update existing product, partial updates allowed
    - GET/POST  /products/<int:id>/deleted
        - delete existing product with id






