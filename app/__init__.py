from flask import Flask
from config import Config

from .blog.routes import blog
from .user.routes import user

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app=Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(user, db)

app.config.from_object(Config)

app.register_blueprint(blog)
app.register_blueprint(user)

from app import routes