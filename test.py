from microblog import app
from flask_testing import TestCase
from flask import url_for
import unittest


class BaseTestCase(TestCase):
    def create_app(self):
        return app

    def test_index_noauth(self):
        response = self.client.get('/', content_type='html/txt')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url_for('login', next='/'))


if __name__ == '__main__':
    unittest.main()
