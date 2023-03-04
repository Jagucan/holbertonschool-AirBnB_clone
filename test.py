#!/usr/bin/python3
import unittest
import datetime
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_BaseModel(unittest.TestCase):
    """ Test for BaseModel Class"""

    def test_to_basemodel_creation(self):
        """ Test for instance creation """
        self.assertIsInstance(BaseModel(), BaseModel)
        self.assertIsInstance(BaseModel().id, str)

    def test_to_str_rep(self):
        """ Test for str instance representation """
        self.assertIsInstance(str(BaseModel()), str)
        self.assertIn("'created_at': {}".format(repr(BaseModel().created_at)), str(BaseModel()))
        self.assertIn("'updated_at': {}".format(repr(BaseModel().updated_at)), str(BaseModel()))

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

class Test_User(unittest.TestCase):
    """ Test for User Class """

    def test_to_user_creation(self):
        """ Test for user instance creation """
        self.assertIsInstance(User(), User)
        self.assertIsInstance(User().email, str)
        self.assertIsInstance(User().password, str)
        self.assertIsInstance(User().first_name, str)
        self.assertIsInstance(User().last_name, str)

class Test_FileStorage(unittest.TestCase):
    """ Test for FileStorage Class """

    def test_to_filestorage_creation(self):
        """ Test for filestorage instance creation """
        self.assertIsInstance(FileStorage(), FileStorage)

if __name__ == '__main__':
    unittest.main()
