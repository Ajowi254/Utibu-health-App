# confirmEmail.py
from flask_restful import Resource
from models.userModel import UserDetails
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os

class confirmEmail(Resource):
    def get(self, token):
        try:
            s = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))
            user_id = s.loads(token, salt='your_salt_here', max_age=3600)
            
            user = UserDetails.find_by_id(user_id)
            if not user:
                return {'statusCode': 400, 'message': 'User not found'}

            user.is_email_confirmed = True
            user.save()

            return {'statusCode': 200, 'message': 'Email confirmed successfully'}
        except SignatureExpired:
            return {'statusCode': 400, 'message': 'The confirmation link has expired'}
        except Exception as error:
            return {'statusCode': 500, 'message': 'Internal Server Error', 'error': str(error)}
