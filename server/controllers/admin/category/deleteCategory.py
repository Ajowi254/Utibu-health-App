#deleteCategory.py
from flask import request
from flask_restful import Resource
from models.category import CategoryDetails

class deleteCategory(Resource):
    def delete(self, id):
        try:
            category_details = CategoryDetails()
            category_details.find_by_id_and_delete(id, request.json)
            return {'statusCode': 200, 'message': 'Category deleted successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Category deletion failed', 'statusCode': 500}
