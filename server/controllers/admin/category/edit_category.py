#editCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails

class edit_category(Resource):
    def put(self, id):
        try:
            category_details = CategoryDetails()
            category_details.find_by_id_and_update(id, request.json)
            return {'statusCode': 200, 'message': 'Category updated successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category update failed', 'statusCode': 500}
