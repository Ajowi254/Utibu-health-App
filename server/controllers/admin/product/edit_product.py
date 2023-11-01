#editproduct.py
from models.product import ProductDetails
from flask import jsonify, request

def edit_product(id):
    try:
        quantity = request.json['quantity']
        doc = ProductDetails.find_by_id(id)
        if quantity != doc['quantity']:
            request.json['availableInStock'] = (quantity - doc['quantity']) + doc['availableInStock']
        product_details = ProductDetails()
        product_details.find_by_id_and_update(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Product updated successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Product update failed',
            'statusCode': 500
        })
