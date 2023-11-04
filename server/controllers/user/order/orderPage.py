#orderpage.py
from flask import request
from flask_restful import Resource
from models.orderModal import OrderDetails
from models.product import ProductDetails

class orderPage(Resource):
    def post(self):
        try:
            order = request.json['order']
            id = OrderDetails.create(request.json)
            for data in order:
                query = data['id']
                doc = ProductDetails.find_by_id(query)
                doc['sold'] += data['quantity']
                doc.save()
                in_stock = ProductDetails.find_by_id(query)
                in_stock['availableInStock'] -= data['quantity']
                in_stock.save()
            return {
                'statusCode': 201,
                'message': 'Order added successfully',
                'id': id['_id']
            }
        except Exception as error:
            return {
                'error': str(error),
                'message': 'Order addition failed',
                'statusCode': 500
            }
