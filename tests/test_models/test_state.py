#!/usr/bin/python3
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """ Test for State Class """

    def test_to_state_creation(self):
        """ Test for user instance creation """
        self.assertIsInstance(State(), State)
        self.assertIsInstance(State().name, str)
