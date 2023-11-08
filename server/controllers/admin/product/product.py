#product.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails

ROWS_PER_PAGE = 5

class product(Resource):
    def get(self):
        try:
            limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
            offset = request.args.get('offset', 0, type=int)
            products = ProductDetails.query.limit(limit).offset(offset).all()
            products_list = [product.to_dict() for product in products]
            return {'data': products_list}, 200
        except Exception as error:
            return str(error), 500

