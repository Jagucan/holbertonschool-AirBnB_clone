#!/usr/bin/python3
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Test for Review Class """

    def test_to_review_creation(self):
        """ Test for review instance creation """
        self.assertIsInstance(Review(), Review)
        self.assertIsInstance(Review().place_id, str)
        self.assertIsInstance(Review().user_id, str)
        self.assertIsInstance(Review().text, str)
