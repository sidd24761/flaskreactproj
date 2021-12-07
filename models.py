from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/searchsample"
db = SQLAlchemy(app)


class Users(db.Model):
    # you can even specify the table name with which you are working.
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique = False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    username=db.Column(db.String(100), unique=False, nullable=False)
class Admins(db.Model):
    # you can even specify the table name with which you are working.
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    # name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique = False, nullable=False)