#category.py
from flask import jsonify, request
from models.category import CategoryDetails

ROWS_PER_PAGE = 5

def category():
    try:
        limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
        offset = request.args.get('offset', 0, type=int)
        categories = CategoryDetails.query.limit(limit).offset(offset).all()
        return jsonify({'data': categories}), 200
    except Exception as error:
        return jsonify(str(error)), 500
