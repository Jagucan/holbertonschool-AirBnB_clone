#!/usr/bin/python3
""" Test for Console """
import unittest
import sys
from unittest.mock import create_autospec
from console import HBNBCommand
import json


class TestHBNBCommand(unittest.TestCase):
    """ Test for Class HBNBCommand """

    def setUp(self):
        """ Metode for the test """
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ Test to quit """
        self.assertTrue(self.console.onecmd("quit"))

    def create(self, server=None):
        """ Test to saving """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

if __name__ == '__main__':
    unittest.main()
