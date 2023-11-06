#dashboardOverview.py
from flask_restful import Resource
from models.product import ProductDetails

class dashboardOverview(Resource):
    def get(self):
        try:
            value = ProductDetails.find()
            bought = sum(item['quantity'] for item in value)
            sold = sum(item['sold'] for item in value)
            out_of_stock = len([item for item in value if item['availableInStock'] == 0])
            total_available_stock = sum(item['availableInStock'] for item in value)

            return {
                'statusCode': 200,
                'totalProducts': len(value),
                'bought': bought,
                'sold': sold,
                'outOfStock': out_of_stock,
                'totalAvailableStock': total_available_stock
            }
        except Exception as error:
            return {
                'error': str(error),
                'message': "Server Side Error",
                'statusCode': 500
            }
