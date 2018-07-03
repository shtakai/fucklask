from app import app
from flask_testing import TestCase
import unittest

class BaseTestCase(TestCase):
    def create_app(self):
        return app

    def test_simple(self):
        self.assertEqual(200, 200)

if __name__ == '__main__':
    unittest.main()
