#product.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class ProductDetails(db.Model):
    __tablename__ = 'product_details'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    product = db.Column(db.String(80), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Integer, default=0)
    productImage = db.Column(db.String(120), nullable=False)
    availableInStock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # relationship
    brand_id = db.Column(db.Integer, db.ForeignKey('brand_details.id'))

    def __repr__(self):
        return '<Product %r>' % self.product
