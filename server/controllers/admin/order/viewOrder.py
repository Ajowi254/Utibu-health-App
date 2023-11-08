#viewOrder.py
from flask import request
from flask_restful import Resource
from models.orderModal import OrderDetails

ROWS_PER_PAGE = 5

class viewOrder(Resource):
    def get(self):
        try:
            limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
            offset = request.args.get('offset', 0, type=int)
            orders = OrderDetails.query.limit(limit).offset(offset).all()
            return {
                'message': 'Order details Send Successfully',
                'data': [order.serialize() for order in orders]
            }, 200
        except Exception as error:
            return {
                'error': str(error),
                'message': 'Internal Server Error',
                'statusCode': 500
            }, 500
