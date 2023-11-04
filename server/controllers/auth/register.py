# register.py
from flask import request
from flask_restful import Resource
import os
from models.userModel import UserDetails
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from .mail import send_email

class register(Resource):
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']

            user = UserDetails.find_one({'email': email})
            if not user:
                hashed_password = generate_password_hash(password)
                new_user = UserDetails.create({'email': email, 'password': hashed_password})

                s = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))
                token = s.dumps(new_user.id, salt='your_salt_here')

                send_email(user.email, token)

                return {
                    'statusCode': 201,
                    'message': 'User registered successfully. Please check your email to confirm your account.'
                }
            else:
                return {
                    'statusCode': 400,
                    'message': 'Email address already exists'
                }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
