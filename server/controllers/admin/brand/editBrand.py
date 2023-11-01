#EditBrand.py
from models.brand import BrandDetails
from flask import jsonify, request

def edit_brand(id):
    try:
        brand_details = BrandDetails()
        brand_details.find_by_id_and_update(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Brand updated successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Brand update failed',
            'statusCode': 500
        })
