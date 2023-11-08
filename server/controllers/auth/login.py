#login.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails
from werkzeug.security import check_password_hash
import jwt
import os

class login(Resource):
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            user = UserDetails.find_one({'email': email})
            if user:
                if check_password_hash(user['password'], password):
                    secret_key = os.environ.get('SECRET_KEY')
                    token = jwt.encode({'id': user['_id'], 'isAdmin': user['isAdmin']}, secret_key, algorithm='HS256')
                    return {
                        'statusCode': 200,
                        'message': 'Login successfully',
                        'token': token,
                        'isAdmin': user['isAdmin'],
                        'name': user['name'],
                        'user': user
                    }
                else:
                    return {
                        'statusCode': 401,
                        'message': 'Password is wrong'
                    }
            else:
                return {
                    'statusCode': 401,
                    'message': 'Invalid email'
                }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
