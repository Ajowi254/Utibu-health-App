#profileDetail.py
from flask_restful import Resource
from models.userModel import UserDetails

class profileDetail(Resource):
    def get(self, id):
        try:
            data = UserDetails.find_by_id(id)
            return {
                'statusCode': 200,
                'message': 'Profile details sent successfully',
                'data': data
            }
        except Exception as error:
            return {
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error)
            }
