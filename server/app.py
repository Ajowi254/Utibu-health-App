# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

# Create the SQLAlchemy and Migrate objects here, but don't bind them to an app yet.
# They will be bound to the Flask app in the create_app function.
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key_here'

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import your models here
    from models.userModel import UserDetails
    from models.orderModal import OrderDetails
    from models.product import ProductDetails
    from models.category import CategoryDetails
    from models.brand import BrandDetails

    # Create an instance of Flask-Restful's Api class
    api = Api(app)

    @app.route('/')
    def home():
     return "Welcome to My Duka App!"

    # Import your resources here
    from controllers.admin.brand.AddBrand import AddBrand
    from controllers.admin.product.editProduct import editProduct
    from controllers.admin.brand.deleteBrand import deleteBrand
    from controllers.admin.brand.editBrand import editBrand
    from controllers.admin.category.addCategory import addCategory
    from controllers.admin.category.deleteCategory import deleteCategory
    from controllers.admin.category.editCategory import editCategory
    from controllers.admin.product.addProduct import addProduct
    from controllers.admin.product.product import product
    from controllers.admin.product.deleteproduct import deleteProduct
    from controllers.admin.product.createProduct import createProduct
    from controllers.admin.user.switchtouser import switchtouser
    from controllers.admin.user.users import users
    from controllers.auth.forgotPassword import forgotPassword
    from controllers.auth.login import login
    from controllers.auth.passwordResetPage import passwordResetPage
    from controllers.auth.register import register
    from controllers.user.order.profileUpdate.profileDetail import profileDetail
    from controllers.user.order.profileUpdate.profileUpdate import profileUpdate
    from controllers.user.order.invoice import invoice
    from controllers.user.order.yourOrder import yourOrder

    # Add your resources to the Api
    api.add_resource(AddBrand, '/brand')
    api.add_resource(editProduct, '/product/<id>')
    api.add_resource(deleteBrand, '/brand/<id>')
    api.add_resource(editBrand, '/brand/<id>')
    api.add_resource(addCategory, '/category')
    api.add_resource(deleteCategory, '/category/<id>')
    api.add_resource(editCategory, '/category/<id>')
    api.add_resource(addProduct, '/product')
    api.add_resource(product, '/product')
    api.add_resource(deleteProduct, '/product/<id>')
    api.add_resource(createProduct, '/product/create')
    api.add_resource(switchtouser, '/user/<id>')
    api.add_resource(users, '/users')
    api.add_resource(forgotPassword, '/forgotPassword')
    api.add_resource(login, '/login')
    api.add_resource(passwordResetPage, '/password-reset')
    api.add_resource(register, '/register')
    api.add_resource(profileDetail, '/profile/<id>')
    api.add_resource(profileUpdate, '/profile/<id>/update')
    api.add_resource(invoice, '/invoice/<id>')
    api.add_resource(yourOrder, '/order/<id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
