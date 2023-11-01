#dashboardProduct.py
from models.product import ProductDetails
from flask import jsonify, request
import re

def dashboard_products():
    try:
        q = request.args.get('q')
        value = ProductDetails.find()
        products = [{'product': item['product'], 'bought': item['quantity'], 'sold': item['sold'], 'availableStock': item['availableInStock']} for item in value]
        
        if not q:
            return jsonify({'statusCode': 200, 'products': products})
        elif re.match(r'^\d*(\.\d+)?$', q):
            data = [item for item in products if item['availableStock'] <= float(q)]
            return jsonify({'statusCode': 200, 'products': data})
        else:
            keys = ['product']
            data = [item for item in products if any(q.lower() in item[key].lower() for key in keys)]
            return jsonify({'statusCode': 200, 'products': data})
    except Exception as error:
        return jsonify({'error': str(error), 'message': "Server Side Error", 'statusCode': 500})
