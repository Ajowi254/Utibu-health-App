#dashboardProduct.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails
import re

class dashboard_product(Resource):
    def get(self):
        try:
            q = request.args.get('q')
            value = ProductDetails.find()
            products = [{'product': item['product'], 'bought': item['quantity'], 'sold': item['sold'], 'availableStock': item['availableInStock']} for item in value]
            
            if not q:
                return {'statusCode': 200, 'products': products}
            elif re.match(r'^\d*(\.\d+)?$', q):
                data = [item for item in products if item['availableStock'] <= float(q)]
                return {'statusCode': 200, 'products': data}
            else:
                keys = ['product']
                data = [item for item in products if any(q.lower() in item[key].lower() for key in keys)]
                return {'statusCode': 200, 'products': data}
        except Exception as error:
            return {'error': str(error), 'message': "Server Side Error", 'statusCode': 500}
