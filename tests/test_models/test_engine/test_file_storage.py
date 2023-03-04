#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """ Test for FileStorage Class """

    def test_to_filestorage_creation(self):
        """ Test for filestorage instance creation """
        self.assertIsInstance(FileStorage(), FileStorage)


if __name__ == '__main__':
    unittest.main()
