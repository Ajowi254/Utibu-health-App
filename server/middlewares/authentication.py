#authentication.py
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash
import jwt
import os
from models.userModel import UserDetails
app = Flask(__name__)
api = Api(app)

# Define a SECRET_KEY in your app configuration.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
class authentication(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data.get('email', None)
            password = data.get('password', None)

            user = UserDetails.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                secret_key = app.config['SECRET_KEY']
                token = jwt.encode({'id': user.id, 'isAdmin': user.isAdmin}, secret_key, algorithm='HS256')

                return {
                    'statusCode': 200,
                    'message': 'Login successfully',
                    'token': token,
                    'isAdmin': user.isAdmin,
                    'name': user.name,
                    'user': user.to_dict()
                }

            else:
                return {
                    'statusCode': 401,
                    'message': 'Invalid email or password',
                }

        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error),
            }