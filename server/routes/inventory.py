# inventory.py
from flask import Blueprint
from controllers.admin.brand.AddBrand import add_brand
from controllers.admin.product.edit_product import edit_product
#from controllers.admin.brand.brand import brand
from controllers.admin.brand.deleteBrand import delete_brand
from controllers.admin.brand.editBrand import edit_brand
from controllers.admin.category.addCategory import add_category
#from controllers.admin.category.category import category
from controllers.admin.category.deleteCategory import delete_category
from controllers.admin.category.editCategory import edit_category
from controllers.admin.product.addproduct import add_product
from controllers.admin.product.product import products
from controllers.admin.product.deleteproduct import delete_product
from controllers.admin.product.create_product import create_product

brand_router = Blueprint('brand', __name__)
category_router = Blueprint('category', __name__)
product_router = Blueprint('product', __name__)

@brand_router.route('/add-brand', methods=['POST'])
def addBrand():
    return add_brand()

#@brand_router.route('/brand', methods=['GET'])
#def getBrand():
    #return brand()

@brand_router.route('/delete-brand/<id>', methods=['DELETE'])
def deleteBrand(id):
    return delete_brand(id)

@brand_router.route('/edit-brand/<id>', methods=['PUT'])
def editBrand(id):
    return edit_brand(id)

@category_router.route('/add-category', methods=['POST'])
def addCategory():
    return add_category()

#@category_router.route('/category', methods=['GET'])
#def getCategory():
    #return category()

@category_router.route('/delete-category/<id>', methods=['DELETE'])
def deleteCategory(id):
    return delete_category(id)

@category_router.route('/edit-category/<id>', methods=['PUT'])
def editCategory(id):
    return edit_category(id)

@product_router.route('/add-product', methods=['POST'])
def addProduct():
    return add_product()

@product_router.route('/products', methods=['GET'])
def getProducts():
    return products()

@product_router.route('/delete-product/<id>', methods=['DELETE'])
def deleteProduct(id):
    return delete_product(id)

@product_router.route('/edit-product/<id>', methods=['PUT'])
def editProduct(id):
    return edit_product(id)

@product_router.route('/create-product', methods=['POST'])
def create_product():
    return create_product()
