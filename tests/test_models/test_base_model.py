#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """ Test for BaseModel Class"""

    def test_to_basemodel_creation(self):
        """ Test for instance creation """
        self.assertIsInstance(BaseModel(), BaseModel)
        self.assertIsInstance(BaseModel().id, str)

    def test_to_str_rep(self):
        """ Test for str instance representation """
        b = BaseModel()
        self.assertIsInstance(str(BaseModel()), str)
        self.assertIn("'created_at': {}".format(repr(b.created_at)), str(b))
        self.assertIn("'updated_at': {}".format(repr(b.updated_at)), str(b))

    def test_to_dict(self):
        """ Test for dict instance method """
        self.assertIsInstance(BaseModel().to_dict(), dict)
        self.assertIn('id', BaseModel().to_dict())
        self.assertIn('created_at', BaseModel().to_dict())
        self.assertIn('updated_at', BaseModel().to_dict())

    def test_to_save(self):
        """ Test for save instance method """
        before = BaseModel().updated_at
        BaseModel().save()
        after = BaseModel().updated_at
        self.assertLess(before, after)
