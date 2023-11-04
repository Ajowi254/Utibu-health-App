#profileUpdate.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails

class profileUpdate(Resource):
    def put(self, id):
        try:
            name = request.json['name']
            email = request.json['email']
            age = request.json['age']
            date_of_birth = request.json['dateOfBirth']
            profile_url = request.json['profileUrl']
            doc = UserDetails.find_by_id(id)
            doc['name'] = name
            doc['email'] = email
            doc['age'] = age
            doc['dateOfBirth'] = date_of_birth
            doc['profileUrl'] = profile_url
            doc.save()
            return {
                'statusCode': 200,
                'message': 'Profile updated successfully'
            }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
