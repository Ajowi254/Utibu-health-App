# DeleteCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails
from app import db

class delete_category(Resource):
    def delete(self, id):
        try:
            category = CategoryDetails.query.get(id)
            if category is None:
                return {'statusCode': 404, 'message': 'Category not found'}
            db.session.delete(category)
            db.session.commit()
            return {'statusCode': 200, 'message': 'Category deleted successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category deletion failed', 'statusCode': 500}
