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

    def test_save_user(self):
            '''
            test if user's info has been saved inthe user's list
            '''
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),1)

class TestPassword(unit.TestCase):
            """
            class defines test cases while testCase  creates a test case
            """
            def test_check_user(self):
                """
                tests whether the login function works as expected
                """
                self.new_user = User ('Drac','Angelo','memedank2')
                self.new_user.save_user()
                user2 = User('Ken','Ng\'ang\'a','murigi')
		        user2.save_user()

if __name__ ==  '__main__':
    unittest.main()