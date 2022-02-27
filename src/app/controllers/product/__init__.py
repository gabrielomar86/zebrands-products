from flask import Blueprint

product = Blueprint('product', __name__, url_prefix='/products')

from . import views