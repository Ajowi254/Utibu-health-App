#addCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails

class addCategory(Resource):
    def post(self):
        try:
            category_details = CategoryDetails()
            category_details.create(request.json)
            return {'statusCode': 201, 'message': 'Category added successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category addition failed', 'statusCode': 500}
