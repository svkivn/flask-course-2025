
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200,
        "content": "Потужний ноутбук з процесором Intel Core i7, 16 ГБ оперативної пам’яті та SSD на 512 ГБ."
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 800,
        "content": "Смартфон із 6.5-дюймовим OLED-дисплеєм, подвійною камерою та акумулятором на 5000 мА·год."
    },
    {
        "id": 3,
        "name": "PC",
        "price": 1800,
        "content": "Настільний комп’ютер для ігор або роботи з графікою: RTX 4070, 32 ГБ RAM, 1 ТБ SSD."
    }
]

class ProductRepository:
    def __init__(self):
        # Тимчасова заглушка з продуктами
        self._products = products

    # --- CRUD ---
    def get_all(self):
        return self._products

    def get_by_id(self, product_id):
        return next((p for p in self._products if p["id"] == product_id), None)

  # Глобальний репозиторій для зручності
product_repo = ProductRepository()
