# # swagger.py

# from flask import Flask
# from flask_restx import Api, Resource, fields
# from werkzeug import cached_property
# from models.brand import BrandDetails
# from models.category import CategoryDetails
# from models.orderModal import OrderDetails
# from models.product import ProductDetails
# from models.userModel import UserDetails
# from datetime import datetime

# app = Flask(__name__)
# api = Api(app, version='1.0', title='myduka', description='containing all lists of inventory')

# # Define models for Swagger documentation
# brand_model = api.model('Brand', {
#     'id': fields.Integer(readOnly=True, description='The brand ID'),
#     'brand': fields.String(required=True, description='Brand name'),
#     'created_at': fields.DateTime(description='Creation date', default=datetime.utcnow())
# })

# category_model = api.model('Category', {
#     'id': fields.Integer(readOnly=True, description='The category ID'),
#     'category': fields.String(required=True, description='Category name'),
#     'created_at': fields.DateTime(description='Creation date', default=datetime.utcnow())
# })

# order_model = api.model('Order', {
#     'id': fields.Integer(readOnly=True, description='The order ID'),
#     'customer': fields.String(required=True, description='Customer details'),
#     'order': fields.String(required=True, description='Order details'),
#     'payment': fields.String(required=True, description='Payment details'),
#     'payment_id': fields.String(description='Payment ID', default='none'),
#     'paymenttype': fields.String(description='Payment type'),
#     'billerName': fields.String(description='Biller name'),
#     'billerId': fields.String(description='Biller ID'),
#     'created_at': fields.DateTime(description='Creation date', default=datetime.utcnow())
# })

# product_model = api.model('Product', {
#     'id': fields.Integer(readOnly=True, description='The product ID'),
#     'brand': fields.String(required=True, description='Product brand'),
#     'category': fields.String(required=True, description='Product category'),
#     'product': fields.String(required=True, description='Product name'),
#     'rate': fields.Float(required=True, description='Product rate'),
#     'quantity': fields.Integer(required=True, description='Product quantity'),
#     'sold': fields.Integer(description='Number of products sold', default=0),
#     'productImage': fields.String(description='Product image URL'),
#     'availableInStock': fields.Integer(description='Available in stock', default=0),
#     'created_at': fields.DateTime(description='Creation date', default=datetime.utcnow())
# })

# user_model = api.model('User', {
#     'id': fields.Integer(readOnly=True, description='The user ID'),
#     'name': fields.String(required=True, description='User name'),
#     'email': fields.String(required=True, description='User email', unique=True),
#     'password': fields.String(required=True, description='User password'),
#     'mobile': fields.Integer(description='User mobile number'),
#     'age': fields.Integer(description='User age'),
#     'dateOfBirth': fields.Date(description='User date of birth'),
#     'profileUrl': fields.String(description='User profile URL'),
#     'isAdmin': fields.String(description='User role', default='none'),
#     'created_at': fields.DateTime(description='Creation date', default=datetime.utcnow())
# })

# # Create an instance of your models
# brands = [BrandDetails(id=1, brand='Brand 1'), BrandDetails(id=2, brand='Brand 2')]
# categories = [CategoryDetails(id=1, category='Category 1'), CategoryDetails(id=2, category='Category 2')]
# orders = [OrderDetails(id=1, customer='Customer 1', order='Order 1', payment='Payment 1'),
#           OrderDetails(id=2, customer='Customer 2', order='Order 2', payment='Payment 2')]
# products = [ProductDetails(id=1, brand='Brand 1', category='Category 1', product='Product 1', rate=10.0, quantity=100),
#             ProductDetails(id=2, brand='Brand 2', category='Category 2', product='Product 2', rate=15.0, quantity=50)]
# users = [UserDetails(id=1, name='User 1', email='user1@example.com', password='password1', mobile=1234567890),
#          UserDetails(id=2, name='User 2', email='user2@example.com', password='password2', mobile=9876543210)]

# # Create routes for Swagger documentation
# @api.route('/brands')
# class BrandList(Resource):
#     @api.marshal_with(brand_model, as_list=True)
#     def get(self):
#         """List all brands."""
#         return brands

# @api.route('/categories')
# class CategoryList(Resource):
#     @api.marshal_with(category_model, as_list=True)
#     def get(self):
#         """List all categories."""
#         return categories

# # Route to list sample categories
# @api.route('/categories/sample')
# class SampleCategoryList(Resource):
#     @api.marshal_list_with(category_model)
#     def get(self):
#         """List sample categories."""
#         return categories[:3]  # Adjust the number as needed

# # Route to list all brands
# @api.route('/brands/all')
# class AllBrandList(Resource):
#     # @api.marshal_with(brand_model, as_list=True)
#     def get(self):
#         """List all brands."""
#         return brands

# # Route to list sample brands
# @api.route('/brands/sample')
# class SampleBrandList(Resource):
#     @api.marshal_list_with(brand_model)
#     def get(self):
#         """List sample brands."""
#         return brands[:2]  # Adjust the number as needed

# if __name__ == '__main__':
#     app.run(debug=True)
