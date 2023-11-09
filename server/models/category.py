# category.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.dbconfig import db

class CategoryDetails(db.Model):
    __tablename__ = 'category_details'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Category %r>' % self.category

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
