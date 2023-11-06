#invoice.py
from flask_restful import Resource
from models.orderModal import OrderDetails

class invoice(Resource):
    def get(self, id):
        try:
            id = OrderDetails.find_by_id(id)
            return {
                'statusCode': 200,
                'message': 'Order Invoice sent successfully',
                'order_id': id['_id'],
                'customer': id['customer'],
                'order': id['order'],
                'payment': id['payment'],
                'payment_id': id['payment_id'],
                'paymenttype': id['paymenttype']
            }
        except Exception as error:
            return {
                'error': str(error),
                'message': 'Order Invoice send failed',
                'statusCode': 500
            }
