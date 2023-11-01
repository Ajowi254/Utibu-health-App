#category.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class CategoryDetails(db.Model):
    __tablename__ = 'category_details'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Category %r>' % self.category
