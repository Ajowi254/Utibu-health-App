#addproduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails
from app import db
class add_product(Resource):
    def post(self):
        try:
            quantity = request.json['quantity']
            request.json['availableInStock'] = quantity
            new_product = ProductDetails(**request.json)
            db.session.add(new_product)
            db.session.commit()
            return {'statusCode': 201, 'message': 'Product added successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Product addition failed', 'statusCode': 500}