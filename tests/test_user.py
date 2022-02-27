from flask import current_app, url_for
from flask_testing import TestCase

from zebrand_product import app

class UserTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['LOGIN_DISABLED'] = True
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_user_blueprint_exists(self):
        self.assertIn('user', self.app.blueprints)

    def test_user_list_get(self):
        response = self.client.get(url_for('user.users'))

        self.assert200(response)

    def test_user_template(self):
        self.client.get(url_for('user.users'))

        self.assertTemplateUsed('users.html')

