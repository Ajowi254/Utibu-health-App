#yourorder.py
from models.orderModal import OrderDetails
from flask import jsonify

def your_order(id):
    try:
        value = OrderDetails.find()
        data = [item for item in value if item['billerId'] == id]
        return jsonify({
            'message': 'Order details sent successfully',
            'data': data
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Internal Server Error',
            'statusCode': 500
        })
