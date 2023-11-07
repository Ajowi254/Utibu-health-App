#AddBrand.py
from flask_restful import Resource
from models.brand import BrandDetails
from flask import jsonify, request

class add_brand(Resource):
    def post(self):
        try:
            brand_details = BrandDetails()
            brand_details.create(request.json)
            return jsonify({
                'statusCode': 201,
                'message': 'Brand added successfully'
            })
        except Exception as error:
            return jsonify({
                'error': str(error),
                'message': 'Brand addition failed',
                'statusCode': 500
            })
