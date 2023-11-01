#user.py
from flask import Flask, jsonify, request, Blueprint
from controllers.admin.user.switchtouser import switch_to_user
from controllers.admin.user.users import user
from controllers.auth.forgotPassword import forgot_password
from controllers.auth.login import login
from controllers.auth.password_reset_page import password_reset_page
from controllers.auth.register import register
from controllers.user.order.profileUpdate.profileDetail import profile_detail
from controllers.user.order.profileUpdate.profileUpdate import profile_page
from functools import wraps

def validate_token(token):
    # Implement your token validation logic here
    # For now, we'll just check if the token is a specific string
    return token == "my_secure_token"

def authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Missing token'}), 403
        if not validate_token(token):
            return jsonify({'message': 'Invalid token'}), 403
        return f(*args, **kwargs)
    return decorated_function

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    return register(request)

@user_bp.route('/login', methods=['POST'])
def login_user():
    return login(request)

@user_bp.route('/forgot-password', methods=['POST'])
def forgotPassword():
    return forgot_password(request)

@user_bp.route('/password-reset-page', methods=['POST'])
@authentication
def reset_password_page():
    return password_reset_page(request)

@user_bp.route('/profilePage/<id>', methods=['POST'])
def update_profile(id):
    return profile_page(id, request)

@user_bp.route('/profileDetail/<id>', methods=['GET'])
def get_profile_detail(id):
    return profile_detail(id)

@user_bp.route('/user-details', methods=['GET'])
def get_user_details():
    return user()

@user_bp.route('/change-user/<id>', methods=['PUT'])
def change_user(id):
    return switch_to_user(id, request)