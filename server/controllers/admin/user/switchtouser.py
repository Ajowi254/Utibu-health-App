from flask import request
from flask_restful import Resource, reqparse
from models.userModel import UserDetails
from app import db

class switchtouser(Resource):
    def put(self, id):
        try:
            # Parse the request parameters
            parser = reqparse.RequestParser()
            parser.add_argument('e', type=str, required=True, help='Role (admin/user) is required')
            args = parser.parse_args()

            # Extract parameters from args
            e = args['e']
            doc = UserDetails.query.get(id)

            # Check if the user exists
            if doc is None:
                return {'statusCode': 404, 'message': 'User not found'}

            # Check if the user is the default admin account
            if doc.email == 'ajowi.beryl@gmail.com':
                return {'statusCode': 401, 'message': 'Default Admin Account, so role cannot be updated'}

            # Validate the role value to prevent unintended changes
            if e.lower() not in ('admin', 'user'):
                return {'statusCode': 400, 'message': 'Invalid role value. Accepted values are "admin" or "user"'}

            # Update the user's role and commit changes to the database
            doc.isAdmin = e
            db.session.commit()

            return {'statusCode': 200, 'message': 'Role updated successfully'}

        except Exception as error:
            return {'statusCode': 500, 'message': 'Internal Server Error', 'error': str(error)}

