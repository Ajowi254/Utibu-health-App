#profileUpdate.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails
from app import db
from datetime import datetime

class profile_update(Resource):
    def put(self, id):
        try:
            name = request.json['name']
            email = request.json['email']
            age = request.json['age']
            date_of_birth = datetime.strptime(request.json['dateOfBirth'], '%Y-%m-%d').date()
            profile_url = request.json['profileUrl']
            
            # Check if the email already exists
            existing_user = UserDetails.query.filter_by(email=email).first()
            if existing_user and existing_user.id != id:
                return {
                    'statusCode': 400,
                    'message': 'Email already in use',
                }

            doc = UserDetails.query.get(id)
            if doc is not None:
                doc.name = name
                doc.email = email
                doc.age = age
                doc.dateOfBirth = date_of_birth
                doc.profileUrl = profile_url
                db.session.commit()
                return {
                    'statusCode': 200,
                    'message': 'Profile updated successfully'
                }
            else:
                return {
                    'statusCode': 404,
                    'message': 'User not found',
                }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
