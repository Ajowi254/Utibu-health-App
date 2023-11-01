# confirm_email.py
import os
from models.userModel import UserDetails
from flask import jsonify, request
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

def confirm_email(token):
    try:
        s = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))
        user_id = s.loads(token, salt='your_salt_here', max_age=3600)
        
        user = UserDetails.find_by_id(user_id)
        if not user:
            return jsonify({
                'statusCode': 400,
                'message': 'User not found'
            })

        # Activate the user's account here
        user.is_email_confirmed = True
        user.save()

        return jsonify({
                'statusCode': 200,
                'message': 'Email confirmed successfully'
            })
    except SignatureExpired:
        return jsonify({
                'statusCode': 400,
                'message': 'The confirmation link has expired'
            })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
