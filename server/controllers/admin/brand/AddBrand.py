#AddBrand.py
from models.brand import BrandDetails
from flask import jsonify, request

def add_brand():
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
