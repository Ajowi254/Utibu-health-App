#password_reset_page.py
from models.userModel import UserDetails
from flask import jsonify, request
from werkzeug.security import generate_password_hash

def password_reset_page():
    try:
        id = request.json['id']
        password = request.json['password']
        hashed_password = generate_password_hash(password)
        UserDetails.find_by_id_and_update(id, {'password': hashed_password})
        return jsonify({
            'statusCode': 200,
            'message': 'Password reset successfully'
        })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
