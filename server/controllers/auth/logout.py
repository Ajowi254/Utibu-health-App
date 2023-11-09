# logout.py
from flask_restful import Resource

class Logout(Resource):
    def post(self):
        # There's no server-side operation needed to log out a user in a stateless API.
        # The token is simply removed on the client side.
        return {'statusCode': 200, 'message': 'Logout successful'}
