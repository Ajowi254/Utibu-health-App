#deleteCategory.py
from models.category import CategoryDetails
from flask import jsonify, request

def delete_category(id):
    try:
        category_details = CategoryDetails()
        category_details.find_by_id_and_delete(id, request.json)
        return jsonify({
            'statusCode': 200,
            'message': 'Category deleted successfully'
        })
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Category deletion failed',
            'statusCode': 500
        })
