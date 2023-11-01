#deleteBrand.py
from models.brand import BrandDetails
from flask import jsonify, request

def delete_brand(id):
    try:
        brand_details = BrandDetails()
        brand_details.find_by_id_and_delete(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Brand deleted successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Brand deletion failed',
            'statusCode': 500
        })
