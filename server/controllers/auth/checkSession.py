# checkSession.py
from flask_restful import Resource
from flask import request
import jwt

class CheckSession(Resource):
    def get(self):
        token = request.headers.get('Authorization')
        try:
            # Replace 'your_secret_key' with your actual secret key
            payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            return {'statusCode': 200, 'message': 'Session is valid', 'userId': payload['id']}
        except jwt.ExpiredSignatureError:
            return {'statusCode': 401, 'message': 'Session has expired'}
        except jwt.InvalidTokenError:
            return {'statusCode': 401, 'message': 'Invalid session token'}
