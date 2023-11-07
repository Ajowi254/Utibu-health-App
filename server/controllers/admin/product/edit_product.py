#editproduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails
from app import db
class edit_product(Resource):
    def put(self, id):
        try:
            quantity = request.json['quantity']
            product = ProductDetails.query.get(id)
            if product:
                for key, value in request.json.items():
                    setattr(product, key, value)
                if 'quantity' in request.json:
                    product.availableInStock = (quantity - product.quantity) + product.availableInStock
                db.session.commit()
                return {'statusCode': 200, 'message': 'Product updated successfully'}
            else:
                return {'statusCode': 404, 'message': 'Product not found'}
        except Exception as error:
            return {'error': str(error), 'message': 'Product update failed', 'statusCode': 500}
