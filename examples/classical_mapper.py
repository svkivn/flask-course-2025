"""
Модуль для демонстрації класичного (imperative) мапінгу SQLAlchemy 2.0 з простим прикладом роботи з SQLite.
Цей файл показує, як:
- створити SQLAlchemy Engine для SQLite,
- описати таблицю через sqlalchemy.Table та MetaData,
- зв'язати (map_imperatively) простий Python-клас User з таблицею,
- виконувати базові операції через Session (insert, select, get),
- створювати таблиці на диску (metadata.create_all).
"""

from sqlalchemy import Table, Column, Integer, String, MetaData, text, select
from sqlalchemy.orm import registry, Session
from sqlalchemy import create_engine


# Створюємо підключення до SQLite бази даних
engine = create_engine("sqlite:///classical_example.db")

# Об'єкт MetaData зберігає інформацію про таблиці
metadata = MetaData()

# Визначаємо таблицю "users" у базі даних
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

# Клас, який представляє запис у таблиці users
class User:
    engine = engine

    def __init__(self, name=None):
        self.name = name

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            #stmt = select(users_table)
            stmt = text("SELECT * FROM users")
            rows = session.execute(stmt).all()   # повертає list[(row,)]
            return rows

    @classmethod
    def get_id(cls, id_):
        with Session(cls.engine) as session:
            return session.get(cls, id_)

# Створюємо реєстр для класичного мапінгу (SQLAlchemy 2.0)
mapper_registry = registry()

# Classical mapping via registry (SQLAlchemy 2.0): прив'язуємо клас User до таблиці users_table
mapper_registry.map_imperatively(User, users_table)

# Створюємо таблиці у базі даних (якщо їх ще немає)
metadata.create_all(engine)

# Usage
with Session(engine) as session:
    user1 = User("Alex")
    user2 = User("Bob")

    session.add_all([user1, user2])
    session.commit()
    print(f"Added users to DB") 

print("All users:")
with Session(engine) as session:
    stmt = select(User.id, User.name) #
    print(stmt)
    result = session.execute(stmt)
    rows = result.fetchall()  # повертає всі результати як список рядків.
    for row in rows:
        print(f"ID: {row.id}, Name: {row.name}")


# user = User.get_id(2)
# print(f"User with ID 2: {user.name}")
# users = User.get_all()
# for row in users:
#     print(f"- {row}")

