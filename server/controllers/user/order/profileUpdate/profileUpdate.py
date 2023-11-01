#profileUpdate.py
from models.userModel import UserDetails
from flask import jsonify, request

def profile_page(id):
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
        return jsonify({
            'statusCode': 200,
            'message': 'Profile updated successfully'
        })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
