#brand.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class BrandDetails(db.Model):
    __tablename__ = 'brand_details'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # relationship
    products = db.relationship('ProductDetails', backref='brand_details', lazy=True)


    def __repr__(self):
        return '<Brand %r>' % self.brand
