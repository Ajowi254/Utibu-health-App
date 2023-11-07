# EditCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails
from app import db

class edit_category(Resource):
    def put(self, id):
        try:
            category = CategoryDetails.query.get(id)
            if category is None:
                return {'statusCode': 404, 'message': 'Category not found'}
            category.category = request.json['category']
            db.session.commit()
            return {'statusCode': 200, 'message': 'Category updated successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category update failed', 'statusCode': 500}
