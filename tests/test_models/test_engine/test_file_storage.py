#!/usr/bin/python3
""" Module FileStorage """
import os
import time
import json
import unittest
import datetime
from os import remove
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


data = storage.all()


class TestFileStorage(unittest.TestCase):
    """ Test for TestFileStorage Class """

    def setUp(self):
        """ Metode to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Destroys created file """
        FileStorage._FileStorage__file_path = "test.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_file_storage_reload_methode(self):
        """ Test for reload method """
        for all_id in data.keys():
            obj = data[all_id]
            print(obj)
            self.assertIsNotNone(obj)

    def test_file_storage_all_method(self):
        """ Test for all method """
        storage = FileStorage()
        storage_dict = storage.all()
        self.assertIsInstance(storage_dict, dict)
        for obj in storage_dict.values():
            self.assertIsInstance(obj, BaseModel)

    def test_file_storage_new_method(self):
        """ Test for new method """
        base = BaseModel()
        storage = FileStorage()
        storage_dict = storage.all()
        key = '{}.{}'.format(type(base).__name__, base.id)
        self.assertTrue(key in storage_dict.keys())

    def test_file_storage_save_method(self):
        """ Test for save method """
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
