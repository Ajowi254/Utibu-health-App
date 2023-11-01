#dashboardOverview.py
from models.product import ProductDetails
from flask import jsonify

def dashboard_overview():
    try:
        value = ProductDetails.find()
        bought = sum(item['quantity'] for item in value)
        sold = sum(item['sold'] for item in value)
        out_of_stock = len([item for item in value if item['availableInStock'] == 0])
        total_available_stock = sum(item['availableInStock'] for item in value)

        return jsonify({
            'statusCode': 200,
            'totalProducts': len(value),
            'bought': bought,
            'sold': sold,
            'outOfStock': out_of_stock,
            'totalAvailableStock': total_available_stock
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': "Server Side Error",
            'statusCode': 500
        })
