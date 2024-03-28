# controllers/product_resource.py
from flask_restful import Resource
from models.product import ProductDetails

class ProductResource(Resource):
    def get(self, id):
        product = ProductDetails.query.get(id)
        if product:
            return product.to_dict(), 200
        else:
            return {'message': 'Product not found'}, 404
