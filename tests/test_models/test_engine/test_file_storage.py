#!/usr/bin/python3
""" FileStorage unittests """
import unittest
import datetime
import time
import os
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage """

    def setUp(self):
        """ Set up test environment """
        self.file_path = "test.json"
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """ Tear down test environment """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_reload_method(self):
        """Test reload method"""
        self.assertEqual(len(self.storage.all()), 4)
        self.model.save()
        self.storage.reload()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertEqual(len(self.storage.all()), 4)
        self.assertIn(key, self.storage.all().keys())

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
        """Test for save method"""
        base = BaseModel()
        key = '{}.{}'.format(type(base).__name__, base.id)
        base_updated_0 = base.updated_at
        storage = FileStorage()
        objs_0 = storage.all()
        dt_0 = objs_0[key].updated_at

        time.sleep(0.0001)
        base.save()

        base_updated_1 = base.updated_at
        objs_1 = storage.all()
        dt_1 = objs_1[key].updated_at

        self.assertNotEqual(base_updated_1, base_updated_0)
        self.assertNotEqual(dt_1, dt_0)

        try:
            with open('file.json', 'r'):
                remove('file.json')
        except FileNotFoundError:
            self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
