from flask import Flask
from .blog.routes import blog
from .user.routes import user
app=Flask(__name__)
app.register_blueprint(blog)
app.register_blueprint(user)
from app import routes