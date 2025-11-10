from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, Table, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
import os


 
# === Правильний базовий шлях ===
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# === Enum для ролей ===
class UserRole(enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

# === Ініціалізація Flask ===
app = Flask(__name__, instance_relative_config=False)
print(basedir, app.instance_path)

# Гарантуємо, що папка instance існує
os.makedirs(app.instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'relationship-example.db')}"
 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#=== Проміжна таблиця Many-to-Many Post <-> Tag ===
post_tags = Table(
    "post_tags",
    db.metadata,
    db.Column("post_id", db.Integer, ForeignKey("posts.id"), primary_key=True),
    db.Column("tag_id", db.Integer, ForeignKey("tags.id"), primary_key=True)
)

# === Моделі ===
class Role(db.Model):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[UserRole] = mapped_column(Enum(UserRole), unique=True, nullable=False)
    users: Mapped[list["User"]] = relationship(back_populates="role")


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(db.String, nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    posts: Mapped[list["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")
    role: Mapped["Role"] = relationship(back_populates="users")


class Profile(db.Model):
    __tablename__ = "profiles"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    bio: Mapped[str] = mapped_column(db.String)
    avatar_url: Mapped[str] = mapped_column(db.String)
    user: Mapped["User"] = relationship(back_populates="profile")


class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(secondary=post_tags, back_populates="posts")


class Tag(db.Model):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    posts: Mapped[list["Post"]] = relationship(secondary=post_tags, back_populates="tags")


# === Створення таблиць та заповнення даними ===
with app.app_context():
    db.drop_all()
    db.create_all()

    # Ролі
    admin_role = Role(name=UserRole.ADMIN)
    user_role = Role(name=UserRole.USER)

    # Користувачі
    user1 = User(email="ok@gmail.com", role=admin_role)
    user2 = User(email="max@gmail.com", role=user_role)

    # # Профілі
    user1.profile = Profile(bio="Адмін сайту", avatar_url="avatar1.png")
    user2.profile = Profile(bio="Звичайний користувач", avatar_url="avatar2.png")

    # # Пости
    post1 = Post(title="Перший пост", user=user1)
    post2 = Post(title="Другий пост", user=user2)

    # # Теги
    tag1 = Tag(name="Python")
    tag2 = Tag(name="Flask")

    # # Зв'язки постів з тегами через append
    post1.tags.append(tag1)
    post1.tags.append(tag2)
    post2.tags.append(tag1)

    # Додавання всіх об'єктів
    db.session.add_all([admin_role, user_role, user1, user2])
    db.session.commit()


# === Flask-ендпоінти у SQLAlchemy 2.0 стилі ===

@app.route("/users")
def get_users():
    session = db.session
    users = session.execute(select(User)).scalars().all()

    result = []
    for u in users:
        result.append({
            "email": u.email,
            "role": u.role.name.value if u.role else None,
            "profile": {
                "bio": u.profile.bio if u.profile else None,
                "avatar": u.profile.avatar_url if u.profile else None
            },
            "posts": [
                {"title": p.title, "tags": [t.name for t in p.tags]}
                for p in u.posts
            ]
        })
    return jsonify(result)


@app.route("/profiles")
def get_profiles():
    session = db.session
    profiles = session.execute(select(Profile)).scalars().all()

    result = []
    for p in profiles:
        result.append({
            "user_email": p.user.email if p.user else None,
            "bio": p.bio,
            "avatar": p.avatar_url
        })
    return jsonify(result)


@app.route("/posts")
def get_posts():
    session = db.session
    posts = session.execute(select(Post)).scalars().all()

    result = []
    for p in posts:
        result.append({
            "title": p.title,
            "author": p.user.email if p.user else None,
            "tags": [t.name for t in p.tags]
        })
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
