#yourorder.py
from flask_restful import Resource
from models.orderModal import OrderDetails

class yourOrder(Resource):
    def get(self, id):
        try:
            value = OrderDetails.find()
            data = [item for item in value if item['billerId'] == id]
            return {
                'message': 'Order details sent successfully',
                'data': data
            }
        except Exception as error:
            return {
                'error': str(error),
                'message': 'Internal Server Error',
                'statusCode': 500
            }
