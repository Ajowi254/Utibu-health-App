#profileDetail.py
from models.userModel import UserDetails
from flask import jsonify

def profile_detail(id):
    try:
        data = UserDetails.find_by_id(id)
        return jsonify({
            'statusCode': 200,
            'message': 'Profile details sent successfully',
            'data': data
        })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
