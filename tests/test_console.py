#!/usr/bin/python3
""" """
import unittest
import sys
from unittest.mock import create_autospec
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ """
        self.assertTrue(self.console.onecmd("quit"))
    
    def create(self, server=None):
        """ """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

if __name__ == '__main__':
    unittest.main()
