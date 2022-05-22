import unittest

from blog.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User('njeri',"test@test.com",'pass')


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.hashed_password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('pass'))