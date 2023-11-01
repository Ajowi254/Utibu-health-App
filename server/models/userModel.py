#usermodel.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.Integer)
    age = db.Column(db.Integer)
    dateOfBirth = db.Column(db.Date)
    profileUrl = db.Column(db.String(120))
    isAdmin = db.Column(db.String(80), default="none")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    orders = db.relationship('OrderDetails', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name
