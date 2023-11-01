#seed.py
# from app import app, db
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
    # Create and populate BrandDetails
    brand1 = BrandDetails(brand="Brand 1")
    brand2 = BrandDetails(brand="Brand 2")
    brand3 = BrandDetails(brand="Brand 3")

    # Create and populate CategoryDetails
    category1 = CategoryDetails(category="Category 1")
    category2 = CategoryDetails(category="Category 2")
    category3 = CategoryDetails(category="Category 3")

    # Create and populate UserDetails
    user1 = UserDetails(
        name="User 1",
        email="user1@example.com",
        password="hashed_password_1",  # Replace with a secure password hash
        mobile=1234567890,
        age=30,
        dateOfBirth=datetime(1993, 1, 15),
        profileUrl="user1_profile_url",
        isAdmin="admin"
    )
    user2 = UserDetails(
        name="User 2",
        email="user2@example.com",
        password="hashed_password_2",  # Replace with a secure password hash
        mobile=9876543210,
        age=25,
        dateOfBirth=datetime(1998, 5, 20),
        profileUrl="user2_profile_url",
        isAdmin="none"
    )
    
    # order1 = OrderDetails(
    #     customer={
    #         "name": "Customer 1",
    #         "email": "customer1@example.com"
    #     },
    #     order={
    #         "items": ["item1", "item2", "item3"],
    #         "total": 100.0
    #     },
    #     payment={
    #         "method": "Credit Card",
    #         "status": "Paid"
    #     },
    #     payment_id="payment123",
    #     paymenttype="Card",
    #     billerName="Biller 1",
    #     billerId="biller123"
    # )

    customer_data = {
    'user_id': 2,  # User ID
    'name': 'User 2',
    'email': 'user2@example.com',
    # Other user-related data
    }

    order_data = {
    'items': ['item1', 'item2', 'item3'],
    'total': 100.0,
    # Other order-related data
    }

    payment_data = {
    'method': 'Credit Card',
    'status': 'Paid',
    # Other payment-related data
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

    # Add data to the database
    db.session.add_all([brand1, brand2, brand3, category1, category2, category3, user1, user2, order, product1, product2])
    db.session.commit()

if __name__ == '__main__':
    from app import create_app

    app = create_app()
    with app.app_context():
        seed_database()