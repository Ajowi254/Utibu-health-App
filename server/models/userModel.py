# usermodel.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
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
    isAdmin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship('OrderDetails', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'mobile': self.mobile,
            'age': self.age,
            'dateOfBirth': self.dateOfBirth.isoformat() if self.dateOfBirth else None,
            'profileUrl': self.profileUrl,
            'isAdmin': self.isAdmin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
