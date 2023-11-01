#addproduct.py
from models.product import ProductDetails
from flask import jsonify, request

def add_product():
    try:
        quantity = request.json['quantity']
        request.json['availableInStock'] = quantity
        product_details = ProductDetails()
        product_details.create(request.json)
        return jsonify({
            'statusCode': 201,
            'message': 'Product added successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Product addition failed',
            'statusCode': 500
        })
