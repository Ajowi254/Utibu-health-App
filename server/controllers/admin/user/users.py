#users.py
from models.userModel import UserDetails
from flask import jsonify

def user():
    try:
        data = UserDetails.find()
        return jsonify({
            'statusCode': 200,
            'message': 'User details sent successfully',
            'data': data
        })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
