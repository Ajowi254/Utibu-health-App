#editCategory.py
from models.category import CategoryDetails
from flask import jsonify, request

def edit_category(id):
    try:
        category_details = CategoryDetails()
        category_details.find_by_id_and_update(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Category updated successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Category update failed',
            'statusCode': 500
        })
