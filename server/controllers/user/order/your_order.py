#yourorder.py
from flask_restful import Resource
from models.orderModal import OrderDetails

class your_order(Resource):
    def get(self, id):
        try:
            value = OrderDetails.query.all()
            data = [item for item in value if item.billerId == id]
            return {
                'message': 'Order details sent successfully',
                'data': [item.to_dict() for item in data]  # Assuming you have a to_dict method to serialize the object
            }
        except Exception as error:
            return {
                'error': str(error),
                'message': 'Internal Server Error',
                'statusCode': 500
            }
