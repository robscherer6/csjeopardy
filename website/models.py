from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

#a Model is just a layout or blueprint for an object that will
# be stored in the database

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #connects answer with user

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #defining columns stored in db (type of column)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    answers = db.relationship('Answer') #every time we answer, add answer id to this answer field