#seed.py
# from app import app, db
from werkzeug.security import generate_password_hash
from app import create_app, db
from models.userModel import UserDetails
from models.orderModal import OrderDetails
from models.category import CategoryDetails
from models.brand import BrandDetails
from models.product import ProductDetails
from datetime import datetime
from sqlalchemy.orm import Session


created_at_string = '2023-10-30 18:53:11.151699'
created_at = datetime.strptime(created_at_string, '%Y-%m-%d %H:%M:%S.%f')

from app import create_app

# Create the Flask app using the create_app function.
app = create_app()

# Use the application context
with app.app_context():
    # Now you can create the session and work within the application context
    from sqlalchemy.orm import Session
    from models.userModel import UserDetails
    from app import db  # Import your SQLAlchemy instance from your app

    session = Session(db.engine)
    user = session.get(UserDetails, 2)

def seed_database():
    admin_user = UserDetails(
        name="Admin User",
        email="ajowi.beryl@gmail.com",
        password=generate_password_hash("mimi2023"),
        isAdmin=True
    )

    user1 = UserDetails(
        name="User 1",
        email="user1@example.com",
        password=generate_password_hash("user1_password"),  # Replace with a secure password hash
        mobile=1234567890,
        age=30,
        dateOfBirth=datetime(1993, 1, 15),
        profileUrl="user1_profile_url",
        isAdmin=False
    )

    user2 = UserDetails(
        name="User 2",
        email="user2@example.com",
        password=generate_password_hash("user2_password"),  # Replace with a secure password hash
        mobile=9876543210,
        age=25,
        dateOfBirth=datetime(1998, 5, 20),
        profileUrl="user2_profile_url",
        isAdmin=False
    )

    brand1 = BrandDetails(brand="Brand 1")
    brand2 = BrandDetails(brand="Brand 2")
    brand3 = BrandDetails(brand="Brand 3")

    category1 = CategoryDetails(category="Category 1")
    category2 = CategoryDetails(category="Category 2")
    category3 = CategoryDetails(category="Category 3")

    customer_data = {
        'user_id': 2,
        'name': 'User 2',
        'email': 'user2@example.com',
    }

    order_data = {
        'items': ['item1', 'item2', 'item3'],
        'total': 100.0,
    }

    payment_data = {
        'method': 'Credit Card',
        'status': 'Paid',
    }

    order = OrderDetails(
        customer=customer_data,
        order=order_data,
        payment=payment_data,
        payment_id='payment123',
        paymenttype='Card',
        billerName='Biller 1',
        billerId='biller123',
        created_at=datetime.utcnow(),
        user_id=2,
    )

    product1 = ProductDetails(
        brand="Brand 1",
        category="Category 1",
        product="Product 1",
        rate=50.0,
        quantity=100,
        productImage="product1.jpg",
        availableInStock=100
    )

    product2 = ProductDetails(
        brand="Brand 2",
        category="Category 2",
        product="Product 2",
        rate=75.0,
        quantity=80,
        productImage="product2.jpg",
        availableInStock=80
    )

    db.session.add_all([admin_user, user1, user2, brand1, brand2, brand3, category1, category2, category3, order, product1, product2])
    db.session.commit()

if __name__ == '__main__':
    from app import create_app

    app = create_app()
    with app.app_context():
        seed_database()
