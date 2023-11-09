#product.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.dbconfig import db

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

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'category': self.category,
            'product': self.product,
            'rate': self.rate,
            'quantity': self.quantity,
            'sold': self.sold,
            'productImage': self.productImage,
            'availableInStock': self.availableInStock,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'brand_id': self.brand_id,
        }
