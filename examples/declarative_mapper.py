# examples/declarative_mapper.py
# Приклад використання Declarative Mapping у SQLAlchemy 2.0

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Integer, create_engine, select

# Створюємо engine — підключення до SQLite бази даних
engine = create_engine("sqlite:///example.db")

# Базовий клас для Declarative Mapping у SQLAlchemy 2.0
class Base(DeclarativeBase):
    pass

# Опис таблиці "users" як класу User. 
# Клас User автоматично пов’язується з таблицею "users".
# Опис колонок за допомогою type hints і mapped_column
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

# Створюємо таблиці у базі даних, якщо їх ще немає
Base.metadata.create_all(engine)

if __name__ == "__main__":
    # Usage
    with Session(engine) as session:
        user1 = User(name="Bob")
        session.add(user1)
        user2 = User(name="Alice")
        session.add(user2)
        session.commit()
        print(f"Added user ") 

    with Session(engine) as session:
        users = session.execute(select(User)).scalars().all()
        users = session.scalars(select(User)).all() 

        print("All users:")
        for user in users:          
            print(f" - {user.id} {user.name}")

    with Session(engine) as session:
        user = session.get(User, 6)
        session.delete(user)   
        session.commit()        
        print(f"Deleted user with ID 6")

    with Session(engine) as session:
        user = session.get(User, 5)
        user.name = "Charlie"
        session.commit()
        print(f"Updated user with ID 5")     

