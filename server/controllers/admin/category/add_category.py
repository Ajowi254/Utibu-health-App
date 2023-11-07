# AddCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails
from app import db

class add_category(Resource):
    def post(self):
        try:
            category = CategoryDetails(category=request.json['category'])
            db.session.add(category)
            db.session.commit()
            return {'statusCode': 201, 'message': 'Category added successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category addition failed', 'statusCode': 500}
