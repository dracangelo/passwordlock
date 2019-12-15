import unittest
from password import Password

class testUser(unittest.TestCase):
    def setUp(self):
    """
    set up to run before each test case.

    """
    self.new_password = Password("user_name","password","email@ms.com") #this creates a new password

    def tearDown(self)
    """cleans up after each case has run