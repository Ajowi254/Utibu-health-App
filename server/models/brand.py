#brand.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
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

    @classmethod
    def find_by_id_and_update(cls, id, data):
        brand = cls.query.get(id)
        if not brand:
            raise Exception('Brand not found')
        for key, value in data.items():
            setattr(brand, key, value)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
