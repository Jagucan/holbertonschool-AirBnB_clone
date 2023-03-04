#!/usr/bin/python3
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Test for State Class """

    def test_to_place_creation(self):
        """ Test for place instance creation """
        self.assertIsInstance(Place(), Place)
        self.assertIsInstance(Place().city_id, str)
        self.assertIsInstance(Place().user_id, str)
        self.assertIsInstance(Place().name, str)
        self.assertIsInstance(Place().description, str)
        self.assertIsInstance(Place().number_rooms, str)
        self.assertIsInstance(Place().number_bathrooms, str)
        self.assertIsInstance(Place().max_guest, str)
        self.assertIsInstance(Place().price_by_night, str)
        self.assertIsInstance(Place().latitude, str)
        self.assertIsInstance(Place().longitude, str)
        self.assertIsInstance(Place().amenity_ids, str)
