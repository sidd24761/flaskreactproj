from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:newpassword@localhost/searchsample"
db = SQLAlchemy(app)


class Users(db.Model):
    # you can even specify the table name with which you are working.
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique = False, nullable=False)


class Admins(db.Model):
    # you can even specify the table name with which you are working.
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    # name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), unique = False, nullable=False)

class Information(db.Model):
    # you can even specify the table name with which you are working.
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key = True, unique=True, nullable=False)
    title = db.Column(db.String(100), unique=False, nullable=False)
    tags = db.Column(db.String(100), unique=True, nullable=False)
    categories = db.Column(db.String(500), unique = False, nullable=False)
    link = db.Column(db.String(100), unique=False, nullable=False)
    type = db.Column(db.String(100), unique=False, nullable=False)
    featured = db.Column(db.String(100), unique=False, nullable=False)
    levels = db.Column(db.String(100), unique=False, nullable=False)
