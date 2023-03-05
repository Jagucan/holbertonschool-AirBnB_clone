""" FileStorage unittests """
import unittest
import datetime
import time
import os
import json
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User

data = storage.all()


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage """

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "test.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_file_storage_reload_method(self):
        """ Empty reload function """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_obj.save()
        my_dict1 = my_obj.all()
        os.remove("test.json")
        my_obj.reload()
        my_dict2 = my_obj.all()
        self.assertTrue(my_dict2 == my_dict1)

    def test_file_storage_all_method(self):
        """Test to all methods"""
        storage = FileStorage()
        storage_dict = storage.all()
        self.assertIsInstance(storage_dict, dict)
        for obj in storage_dict.values():
            self.assertIsInstance(obj, BaseModel)

    def test_file_storage_new_method(self):
        """Test to new method"""
        base = BaseModel()
        storage = FileStorage()
        storage_dict = storage.all()
        key = '{}.{}'.format(type(base).__name__, base.id)
        self.assertTrue(key in storage_dict.keys())

    def test_file_storage_save_method(self):
        """ Tests the save method for filestorage """
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict1 = my_obj.all()
        my_obj.save()
        my_obj.reload()
        my_dict2 = my_obj.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())

        os.remove('test.json')

if __name__ == '__main__':
    unittest.main()
