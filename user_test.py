import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    """
    testcase helps in createng text cases
    """
    def setUp(self):
            """
            create a user account before each test
            """
            self.new user = User('Drac','Angelo','memedank2')
