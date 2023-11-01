#login.py
from models.userModel import UserDetails
from flask import jsonify, request
from werkzeug.security import check_password_hash
import jwt
import os

def login():
    try:
        email = request.json['email']
        password = request.json['password']
        user = UserDetails.find_one({'email': email})
        if user:
            if check_password_hash(user['password'], password):
                token = jwt.encode({'id': user['_id']}, os.environ.get('SECRET_KEY'), algorithm='HS256')
                return jsonify({
                    'statusCode': 201,
                    'message': 'Login successfully',
                    'token': token,
                    'isAdmin': user['isAdmin'],
                    'name': user['name'],
                    'user': user
                })
            else:
                return jsonify({
                    'statusCode': 401,
                    'message': 'Password is wrong'
                })
        else:
            return jsonify({
                'statusCode': 401,
                'message': 'Invalid email'
            })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
