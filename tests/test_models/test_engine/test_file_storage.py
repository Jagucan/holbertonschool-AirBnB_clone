#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage, BaseModel


class Test_FileStorage(unittest.TestCase):
    """ Test for FileStorage Class"""

    def setUp(self):
        """ Set up test environment """
        self.__file_path = "test.json"
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_to_all(self):
        """ Test for all method """
        self.assertEqual(len(self.storage.all()), 0)
        self.model.save()
        self.assertEqual(len(self.storage.all()), 1)

    def test_to_new(self):
        """ Test for new method """
        self.storage.new(self.model)
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(key, self.storage.all().keys())

    def test_to_save(self):
        """ Test for save method """
        self.assertEqual(len(self.storage.all()), 0)
        self.model.save()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        with open(self.__file_path, "r") as f:
            data = f.read()
        self.assertIn(key, data)

    def test_to_reload(self):
        """ Test for reload method """
        self.assertEqual(len(self.storage.all()), 0)
        self.model.save()
        self.storage.reload()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(key, self.storage.all().keys())

if __name__ == '__main__':
    unittest.main()
