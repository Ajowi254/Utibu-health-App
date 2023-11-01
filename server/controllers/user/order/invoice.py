#invoice.py
from models.orderModal import OrderDetails
from flask import jsonify

def invoice(id):
    try:
        id = OrderDetails.find_by_id(id)
        return jsonify({
            'statusCode': 200,
            'message': 'Order Invoice sent successfully',
            'order_id': id['_id'],
            'customer': id['customer'],
            'order': id['order'],
            'payment': id['payment'],
            'payment_id': id['payment_id'],
            'paymenttype': id['paymenttype']
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Order Invoice send failed',
            'statusCode': 500
        })
