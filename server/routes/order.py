
# order.py
from flask import Blueprint, request
from controllers.admin.order.viewOrder import view_order
from controllers.user.order.invoice import invoice
from controllers.user.order.orderPage import order
from controllers.user.order.yourOrder import your_order

order_bp = Blueprint('order', __name__)

@order_bp.route('/order', methods=['POST'])
def place_order():
    return order(request)

@order_bp.route('/invoice/<id>', methods=['GET'])
def get_invoice(id):
    return invoice(id)

@order_bp.route('/view-order', methods=['GET'])
def get_view_order():
    return view_order()

@order_bp.route('/your-order/<id>', methods=['GET'])
def get_your_order(id):
    return your_order(id)