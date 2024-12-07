from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class BonClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    e1 = db.Column(db.Integer)
    e2 = db.Column(db.Integer)
    e3 = db.Column(db.Integer)
    e4 = db.Column(db.Integer)
    e5 = db.Column(db.Integer)
    e6 = db.Column(db.Integer)
    e7 = db.Column(db.Integer)
    e8 = db.Column(db.Integer)
    c1 = db.Column(db.Integer)
    c2 = db.Column(db.Integer)
    c3 = db.Column(db.Integer)
    c4 = db.Column(db.Integer)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    promo_type = db.Column(db.String(50))
    e1 = db.Column(db.Integer)
    e2 = db.Column(db.Integer)
    e3 = db.Column(db.Integer)
    e4 = db.Column(db.Integer)
    e5 = db.Column(db.Integer)
    e6 = db.Column(db.Integer)
    e7 = db.Column(db.Integer)
    e8 = db.Column(db.Integer)
    c = db.Column(db.String(2)) # c1,c2,c3,c4

