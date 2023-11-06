#switchtouser.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails

class switchtouser(Resource):
    def put(self, id):
        try:
            e = request.json['e']
            doc = UserDetails.find_by_id(id)
            if doc['email'] == 'ajowi.beryl@gmail.com':
                return {'statusCode': 401, 'message': 'Default Admin Account, So Role Does Not Update'}
            else:
                doc['isAdmin'] = e
                doc.save()
                return {'statusCode': 200, 'message': 'Role updated successfully'}
        except Exception as error:
            return {'statusCode': 500, 'message': 'Internal Server Error', 'error': str(error)}
