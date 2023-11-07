#deleteproduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails

from app import db

class delete_product(Resource):
    def delete(self, id):
        try:
            product = ProductDetails.query.get(id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return {'statusCode': 200, 'message': 'Product deleted successfully'}
            else:
                return {'statusCode': 404, 'message': 'Product not found'}
        except Exception as error:
            return {'error': str(error), 'message': 'Product deletion failed', 'statusCode': 500}