# pip install -U Flask-SQLAlchemy

import select

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Integer(15), unique=True)
    email: Mapped[str]


# CREATE TABLE
with app.app_context():
    #Base.metadata.create_all(db.engine)

    #Метод db.create_all() лише створює таблиці, яких ще немає в базі даних.
    # Він не змінює структуру вже створених таблиць.
    db.create_all()

    db.session.add(User(username="example"))
    db.session.commit()

    users = db.session.scalars(select(User))

    for user in users:
        print(f"User: {user.username}, Email: {user.email}")    