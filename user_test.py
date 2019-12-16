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
        self.new_user = User('Drac', 'Angelo', 'memedank2')

    def test__init__(self):
        """
        test if the initialization of the user has been done correctly
        """
        self.assertEqual(self.new_user.first_name, 'Drac')
        self.assertEqual(self.new_user.last_name, 'Angelo')
        self.assertEqual(self.new_password.password, 'memedank2')

    def test_save_user(self):
        '''
        test if user's info has been saved inthe user's list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestPassword(unit.TestCase):
    """
    class defines test cases while testCase  creates a test case
    """


	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('drac','Angelo','memedank2')
		self.new_user.save_user()
		user2 = User('Ken','Ng\'ang\'a','murigi')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def setUp(self):
        """
        creates a password for the account before each test
        """
        self.new_password = password('Drac','instagram','Alucard','vokeee')

    def test__init__(self):
        '''
        test if initialization of password is done correctly done
        '''
        self.assertEqual(self.new_password.user_name,'Drac')
        self.assertEqual(self.new_password.user.media_name,'instagram')
        self.assertEqual(self.new_password.user.account_name,'Alucard')
        self.assertEqual(self.new_password.password,'vokeee')

    def test_save_password(self):
        '''
        check if password is saved in password array
        '''
        self.new_password.test_save_password()
        reddit = password('vokee','reddit','dankmemmer','memememe')
        reddit.save_password()
        self.assertEqual(len(Password.password_list), 2)

	def tearDown(self):
        '''
        this clears the password list after test
        '''
        Password.password_list = []
        User.user_list =[]

    def test_display_password(self):
        '''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
        self.new_password.save_password()
        reddit = password('vokee','reddit','dankmemmer','memememe')
        reddit.save_password()
        gmail = password('Jane','Gmail','maryjoe','pswd200')
		gmail.save_password()
        self.assertEqual(len(password.display_password(reddit.user_name), 2))

if __name__ == '__main__':
    unittest.main()