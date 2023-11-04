#users.py
from flask import request
from flask_restful import Resource
from models.userModel import UserDetails

ROWS_PER_PAGE = 5  

class users(Resource):
    def get(self):
        try:
            limit = request.args.get('limit', ROWS_PER_PAGE, type=int)
            offset = request.args.get('offset', 0, type=int)
            users = UserDetails.query.limit(limit).offset(offset).all()
            users_list = [user.to_dict() for user in users]
            return {'data': users_list}, 200
        except Exception as error:
            return str(error), 500
