from flask import flash, render_template, session
from flask_login import current_user
from src.infrastructure.repositories.product_repository import ProductRepository
from . import product  

@product.route('/', methods=['GET'])
def products():
    prod = ProductRepository()
    
    context = {
        'products': prod.get_all_products(),
    }

    return render_template('products.html', **context)