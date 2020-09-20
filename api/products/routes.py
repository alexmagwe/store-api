from . import products
from flask import jsonify
from .. models import Products
@products.route('all',methods=['GET'])
def all():
    products=Products.query.all()
    return jsonify([{'name':product.name,'price':product.price,'in-stock':product.getQuantity()} for product in products])

