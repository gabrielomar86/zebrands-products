from flask import current_app, url_for
from flask_testing import TestCase

from zebrand_product import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['LOGIN_DISABLED'] = True
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
        
    def test_index_redirect_to_hello(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello_world'))
        
    def test_product_hello_template(self):
        self.client.get(url_for('hello_world'))
        
        self.assertTemplateUsed('hello.html')
        
    def test_hello_get_return_200(self):
        response = self.client.get(url_for('hello_world'))
        self.assert200(response)
        
    def test_hello_post_redirect_return_405_not_allowed(self):
        response = self.client.post(url_for('hello_world'))
        self.assert405(response)
