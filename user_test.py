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

    def test__init__(self):
            """
            test if the initialization of the user has been done correctly
            """
            self.assertEqual(self.new_user.first_name,'Drac')
            self.assertEqual(self.new_user.last_name,'Angelo')
            self.assertEqual(self.new_password.password,'memedank2')
