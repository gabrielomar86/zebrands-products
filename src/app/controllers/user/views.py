from flask import flash, render_template
from flask_login import login_required
from src.app.forms.user_form import UserForm
from src.infrastructure.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.user_repository import UserRepository
from . import user  

@user.route('/', methods=['GET'])
@login_required
def users():
    userRepository = UserRepository()
    user_form = UserForm()
    context = {
        'users': userRepository.get_users(),
        'user_form': user_form,
    }

    return render_template('users.html', **context)