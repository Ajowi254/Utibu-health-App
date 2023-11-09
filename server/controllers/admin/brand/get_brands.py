#brand.py
from flask import request
from flask_restful import Resource
from models.brand import BrandDetails

ROWS_PER_PAGE = 5

class get_brands(Resource):
    def get(self):
        try:
            limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
            offset = request.args.get('offset', 0, type=int)
            brands = BrandDetails.query.limit(limit).offset(offset).all()
            return {'data': [brand.to_dict() for brand in brands]}, 200
        except Exception as error:
            return str(error), 500
