#create_product.py
import cloudinary.uploader
from flask import jsonify, request
from models.product import ProductDetails
from app import db

cloudinary.config(
  cloud_name = 'du0kjb5is',  
  api_key = '396637493398753',  
  api_secret = 'cZNbH3XKKKk48_XgTkf5if-DsSU'  
)

def create_product():
    try:
        # Get the image file from the request
        image_file = request.files.get('productImage')

        # Upload the image file to Cloudinary
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file)
            # Get the URL of the uploaded image
            image_url = upload_result['url']

            # Create a new product with the uploaded image URL
            product = ProductDetails(productImage=image_url)
            db.session.add(product)
            db.session.commit()

        return jsonify({'message': 'Product created successfully'}), 200
    except Exception as error:
        return jsonify(str(error)), 500
