#invoice.py
from flask_restful import Resource
from models.orderModal import OrderDetails

class invoice(Resource):
    def get(self, id):
        try:
            order = OrderDetails.query.get(id)
            if order is not None:
                return {
                    'statusCode': 200,
                    'message': 'Order Invoice sent successfully',
                    'order_id': order.id,
                    'customer': order.customer,
                    'order': order.order,
                    'payment': order.payment,
                    'payment_id': order.payment_id,
                    'paymenttype': order.paymenttype
                }
            else:
                return {
                    'statusCode': 404,
                    'message': 'Order not found',
                }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
