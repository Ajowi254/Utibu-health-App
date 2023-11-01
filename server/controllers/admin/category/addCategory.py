#addCategory.py
from models.category import CategoryDetails
from flask import jsonify, request

def add_category():
    try:
        category_details = CategoryDetails()
        category_details.create(request.json)
        return jsonify({
            'statusCode': 201,
            'message': 'Category added successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Category addition failed',
            'statusCode': 500
        })
