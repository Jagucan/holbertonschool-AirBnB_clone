
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ """
        self.assertTrue(self.console.onecmd("quit"))

    def test_emptyline(self):
        """ """
        self.assertEqual(None, self.console.onecmd(""))

if __name__ == '__main__':
    unittest.main()
