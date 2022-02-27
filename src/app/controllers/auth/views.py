from flask import flash, redirect, render_template, session, url_for
from flask_login import login_required, login_user, logout_user
from src.app.forms.login_form import LoginForm
from src.domain.model.user_model import UserData, UserModel
from src.infrastructure.repositories.user_repository import UserRepository
from . import auth  
from werkzeug.security import check_password_hash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        password = login_form.password.data
        
        user_repository = UserRepository()
        user_doc = user_repository.get_user_by_username(user_name)

        if user_doc is not None:
            session['user_name'] = user_name
            if check_password_hash(user_doc.password, password):
                user_data = UserData(user_doc.email, user_doc.username, user_doc.password, user_doc.is_admin)
                user_model = UserModel(user_data)
                
                login_user(user_model)
                
                flash('Login Successful!', 'success')
                
                return redirect(url_for('hello_world'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        else:    
            flash('Login Unsuccessful. Please check username and password', 'danger')
        
        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))