#orderpage.py
from models.orderModal import OrderDetails
from models.product import ProductDetails
from flask import jsonify, request

def order():
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
        return jsonify({
            'statusCode': 201,
            'message': 'Order added successfully',
            'id': id['_id']
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Order addition failed',
            'statusCode': 500
        })
