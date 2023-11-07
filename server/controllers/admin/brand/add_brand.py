# AddBrand.py
from flask import request
from flask_restful import Resource
from models.brand import BrandDetails
from app import db

class add_brand(Resource):
    def post(self):
        try:
            brand = BrandDetails(brand=request.json['brand'])
            db.session.add(brand)
            db.session.commit()
            return {'statusCode': 201, 'message': 'Brand added successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Brand addition failed', 'statusCode': 500}
