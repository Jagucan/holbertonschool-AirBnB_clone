#!/usr/bin/python3
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """ Test for User Class """

    def test_to_user_creation(self):
        """ Test for user instance creation """
        self.assertIsInstance(User(), User)
        self.assertIsInstance(User().email, str)
        self.assertIsInstance(User().password, str)
        self.assertIsInstance(User().first_name, str)
        self.assertIsInstance(User().last_name, str)
