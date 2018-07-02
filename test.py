from app import app
from flask_testing import TestCase
import unittest

class BaseTestCase(TestCase):
    def create_app(self):
        return app

    def test_render(self):
        response = self.client.get('/', content_type='html/txt')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'aHome page for fucked up page', response.data)

if __name__ == '__main__':
    unittest.main()
