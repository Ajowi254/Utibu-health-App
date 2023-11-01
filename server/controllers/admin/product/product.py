#product.py
from flask import jsonify, request
from models.product import ProductDetails

ROWS_PER_PAGE = 5

def products():
    try:
        limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
        offset = request.args.get('offset', 0, type=int)
        products = ProductDetails.query.limit(limit).offset(offset).all()
        return jsonify({'data': products}), 200
    except Exception as error:
        return jsonify(str(error)), 500
