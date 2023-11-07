#editproduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails

class edit_product(Resource):
    def put(self, id):
        try:
            quantity = request.json['quantity']
            doc = ProductDetails.find_by_id(id)
            if quantity != doc['quantity']:
                request.json['availableInStock'] = (quantity - doc['quantity']) + doc['availableInStock']
            product_details = ProductDetails()
            product_details.find_by_id_and_update(id, request.json)
            return {'statusCode': 200, 'message': 'Product updated successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Product update failed', 'statusCode': 500}
