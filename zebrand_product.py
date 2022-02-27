import unittest
from flask import jsonify, render_template, request, make_response, redirect, session
from flask_login import current_user, login_required

from src.app import create_app

(app, db) = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/create')
def create():
    return '<h1>Create</h1>'

#FLASK_ENV=development FLASK_APP=zebrand-product.py FLASK_DEBUG=1 flask run
@app.route('/hello', methods=['GET'])
@login_required
def hello_world():
    context = {
        'current_user': current_user
    }
        
    return render_template('hello.html', **context)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    
    return response
