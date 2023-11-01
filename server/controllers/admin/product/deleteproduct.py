#deleteproduct.py
from models.product import ProductDetails
from flask import jsonify, request

def delete_product(id):
    try:
        product_details = ProductDetails()
        product_details.find_by_id_and_delete(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Product deleted successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Product deletion failed',
            'statusCode': 500
        })
