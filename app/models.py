from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

# Create Models based off of ERD (Database Tables)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False, unique=True)
    last_name = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    NBAPlayer = db.relationship('NBAPlayer', backref='author', lazy=True)
    
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

class NBAPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False, unique=True)
    last_name = db.Column(db.String(150), nullable=False, unique=True)
    strengths= db.Column(db.String(150), nullable=False, unique=True)
    weakness = db.Column(db.String(150), nullable=False, unique=True)

    def __init__(self, first_name, last_name, strengths, weakness):
        self.first_name = first_name
        self.last_name = last_name
        self.strengths = strengths
        self.weakness = weakness
        
