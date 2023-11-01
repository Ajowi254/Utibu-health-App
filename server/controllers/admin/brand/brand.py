#brand.py
from flask import jsonify, request
from models.brand import BrandDetails

ROWS_PER_PAGE = 5

def brand():
    try:
        limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
        offset = request.args.get('offset', 0, type=int)
        brands = BrandDetails.query.limit(limit).offset(offset).all()
        return jsonify({'data': brands}), 200
    except Exception as error:
        return jsonify(str(error)), 500

