#create_product.py
from flask import request
from flask_restful import Resource
from models.product import ProductDetails
from app import db
import cloudinary.uploader

cloudinary.config(
  cloud_name = 'du0kjb5is',  
  api_key = '396637493398753',  
  api_secret = 'cZNbH3XKKKk48_XgTkf5if-DsSU'  
)

class create_product(Resource):
    def post(self):
        try:
            image_file = request.files.get('productImage')
            if image_file:
                upload_result = cloudinary.uploader.upload(image_file)
                image_url = upload_result['url']
                product = ProductDetails(productImage=image_url)
                db.session.add(product)
                db.session.commit()
            return {'message': 'Product created successfully'}, 200
        except Exception as error:
            return str(error), 500
