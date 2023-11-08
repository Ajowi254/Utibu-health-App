# DeleteBrand.py
from flask import request
from flask_restful import Resource
from models.brand import BrandDetails
from app import db

class delete_brand(Resource):
    def delete(self, id):
        try:
            brand = BrandDetails.query.get(id)
            if brand is None:
                return {'statusCode': 404, 'message': 'Brand not found'}
            db.session.delete(brand)
            db.session.commit()
            return {'statusCode': 200, 'message': 'Brand deleted successfully'}
        except Exception as error:
            return {'error': str(error), 'message': 'Brand deletion failed', 'statusCode': 500}
