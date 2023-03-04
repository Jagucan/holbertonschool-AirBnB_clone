#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Test for Amenity Class """

    def test_to_amenity_creation(self):
        """ Test for user instance creation """
        self.assertIsInstance(Amenity(), Amenity)
        self.assertIsInstance(Amenity().name, str)
