# app.py
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Create the SQLAlchemy and Migrate objects here, but don't bind them to an app yet.
# They will be bound to the Flask app in the create_app function.
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key_here'

    # Bind the SQLAlchemy and Migrate objects to the Flask app.
    db.init_app(app)
    migrate.init_app(app, db)


    # Import your models and routes here
    from models.userModel import UserDetails
    from models.orderModal import OrderDetails
    from models.product import ProductDetails

    # Import your routes modules here
    from routes import inventory, order, user

    # Register your blueprints here
    app.register_blueprint(inventory.brand_router)
    app.register_blueprint(inventory.category_router)
    app.register_blueprint(inventory.product_router)
    app.register_blueprint(order.order_bp)
    app.register_blueprint(user.user_bp)

    @app.route('/')
    def home():
        return "Welcome to My Duka App!"

    return app

if __name__ == '__main__':
    # Create the Flask app using the create_app function and run it.
    app = create_app()
    app.run(debug=True)