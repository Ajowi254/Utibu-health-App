#deleteproduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails

class delete_product(Resource):
    def delete(self, id):
        try:
            product_details = ProductDetails()
            product_details.find_by_id_and_delete(id, request.json)
            return {'statusCode': 200, 'message': 'Product deleted successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Product deletion failed', 'statusCode': 500}
