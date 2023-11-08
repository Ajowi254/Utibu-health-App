# register.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails
from werkzeug.security import generate_password_hash
from app import db

class register(Resource):
    def post(self):
        try:
            data = request.get_json()
            name = data.get('name', None)
            email = data.get('email', None)
            password = data.get('password', None)

            user = UserDetails.query.filter_by(email=email).first()

            if not user:
                hashed_password = generate_password_hash(password)
                new_user = UserDetails(name=name, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

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
