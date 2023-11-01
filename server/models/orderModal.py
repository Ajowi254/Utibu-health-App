#ordermodal.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class OrderDetails(db.Model):
    __tablename__ = 'order_details'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.JSON, nullable=False)
    order = db.Column(db.JSON, nullable=False)
    payment = db.Column(db.JSON, nullable=False)
    payment_id = db.Column(db.String(80), default="none")
    paymenttype = db.Column(db.String(80))
    billerName = db.Column(db.String(80))
    billerId = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user_details.id'), nullable=False)


    def __repr__(self):
        return '<Order %r>' % self.id
