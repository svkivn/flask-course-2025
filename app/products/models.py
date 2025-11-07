from .. import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Product(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Product {self.name} - ${self.price}>"
    
    def __str__(self) -> str:
        return f"<Product {self.name} - ${self.price}>"