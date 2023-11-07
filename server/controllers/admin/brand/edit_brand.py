#EditBrand.py
from flask import request
from flask_restful import Resource
from models.brand import BrandDetails

class edit_brand(Resource):
    def put(self, id):
        try:
            BrandDetails.find_by_id_and_update(id, request.json)
            return {'statusCode': 200, 'message': 'Brand updated successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Brand update failed', 'statusCode': 500}