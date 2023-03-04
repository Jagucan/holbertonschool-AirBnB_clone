#!/usr/bin/python3
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """ Test for City Class """

    def test_to_city_creation(self):
        """ Test for user instance creation """
        self.assertIsInstance(City(), City)
        self.assertIsInstance(City().name, str)
        self.assertIsInstance(City().state_id, str)
