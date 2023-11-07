#profileDetail.py
from flask_restful import Resource
from models.userModel import UserDetails

class profile_detail(Resource):
    def get(self, id):
        try:
            data = UserDetails.query.get(id)
            if data is not None:
                return {
                    'statusCode': 200,
                    'message': 'Profile details sent successfully',
                    'data': data.to_dict()  # Assuming you have a to_dict method to serialize the object
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
