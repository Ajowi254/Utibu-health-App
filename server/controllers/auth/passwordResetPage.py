#password_reset_page.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails
from werkzeug.security import generate_password_hash

class passwordResetPage(Resource):
    def put(self):
        try:
            id = request.json['id']
            password = request.json['password']
            hashed_password = generate_password_hash(password)
            UserDetails.find_by_id_and_update(id, {'password': hashed_password})
            return {
                'statusCode': 200,
                'message': 'Password reset successfully'
            }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
