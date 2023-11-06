#deleteBrand.py
from flask import request
from flask_restful import Resource
from models.brand import BrandDetails

class deleteBrand(Resource):
    def delete(self, id):
        try:
            brand_details = BrandDetails()
            brand_details.find_by_id_and_delete(id, request.json)
            return {'statusCode': 200, 'message': 'Brand deleted successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Brand deletion failed', 'statusCode': 500}
