from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Boolean
from datetime import datetime
from sqlalchemy import DateTime, func

class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)

    # Зв'язок з продуктами (один до багатьох)
    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
        lazy="select"  # або 'dynamic' / 'joined'
    )

class Product(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    # created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, 
    #                                                   server_default=func.now(),   
    #                                              )
    
    category_id: Mapped[int | None] = mapped_column(db.ForeignKey('categories.id'))
    category: Mapped["Category"] = relationship("Category", back_populates="products")

    def __repr__(self) -> str:
        return f"<Product {self.name} - ${self.price}>"
    
    # def __str__(self) -> str:
    #     return f"<Product {self.name} - ${self.price}>"