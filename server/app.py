# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from models.dbconfig import db
from config import Config


def create_app(config_class=Config):
    # Create the Flask application
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    api = Api(app)

    
    # Configure the Flask application
    app.config.from_object(config_class)


    # Initialize the extensions
    db.init_app(app)
    Migrate(app, db)

    # Import your models here
    from models.userModel import UserDetails
    from models.orderModal import OrderDetails
    from models.product import ProductDetails
    from models.category import CategoryDetails
    from models.brand import BrandDetails

    @app.route('/')
    def home():
     return "Welcome to My Duka App!"

    # Import your resources here
    from controllers.admin.brand.add_brand import add_brand
    from controllers.admin.brand.get_brands import get_brands
    from controllers.admin.brand.delete_brand import delete_brand
    from controllers.admin.brand.edit_brand import edit_brand
    from controllers.admin.category.add_category import add_category
    from controllers.admin.category.category import category
    from controllers.admin.category.delete_category import delete_category
    from controllers.admin.category.edit_category import edit_category
    from controllers.admin.product.add_product import add_product
    from controllers.admin.product.product import product
    from controllers.admin.product.delete_product import delete_product
    from controllers.admin.product.create_product import create_product
    from controllers.admin.product.edit_product import edit_product
    from controllers.admin.user.switchtouser import switchtouser
    from controllers.admin.user.users import users
    from controllers.auth.forgot_password import forgot_password
    from controllers.auth.login import login
    from middlewares.authentication import authentication
    from controllers.auth.checkSession import CheckSession
    from controllers.auth.passwordResetPage import passwordResetPage
    from controllers.auth.register import register
    from controllers.user.order.profileUpdate.profile_detail import profile_detail
    from controllers.user.order.profileUpdate.profile_update import profile_update
    from controllers.user.order.invoice import invoice
    from controllers.user.order.your_order import your_order
    from controllers.admin.dashboard.dashboard_overview import dashboard_overview
    from controllers.admin.dashboard.bar_chart import bar_chart
    from controllers.admin.dashboard.dashboard_product import dashboard_product
    from controllers.auth.logout import Logout

    # Add your resources to the Api
    api.add_resource(add_brand, '/brand')#
    api.add_resource(get_brands, '/brands')#
    api.add_resource(delete_brand, '/brand/<int:id>')#
    api.add_resource(edit_brand, '/brand/<int:id>')#
    api.add_resource(add_category, '/addCategory')#
    api.add_resource(category, '/category')#
    api.add_resource(delete_category, '/category/<int:id>')#
    api.add_resource(edit_category, '/category/<int:id>')#
    api.add_resource(add_product, '/addProduct')#
    api.add_resource(edit_product, '/product/<int:id>')#
    api.add_resource(product, '/product')#
    api.add_resource(delete_product, '/product/<id>')#
    api.add_resource(create_product, '/product/create')#
    api.add_resource(switchtouser, '/user/<id>')#
    api.add_resource(users, '/users')#
    api.add_resource(forgot_password, '/forgotPassword')###
    api.add_resource(authentication, '/login')#
    api.add_resource(CheckSession, '/check-session')#
    api.add_resource(passwordResetPage, '/password-reset')###
    api.add_resource(register, '/register')#
    api.add_resource(profile_detail, '/profile/<int:id>')#
    api.add_resource(profile_update, '/profile/<int:id>/update')#
    api.add_resource(invoice, '/invoice/<int:id>')#
    api.add_resource(your_order, '/order/<int:id>')#
    api.add_resource(dashboard_overview, '/dashboardoverview')#
    api.add_resource(bar_chart, '/dashboardbarchart')###
    api.add_resource(dashboard_product, '/dashboardproduct')#
    api.add_resource(Logout, '/logout')#

    return app
if __name__ == '__main__':
    create_app().run(debug=True)
