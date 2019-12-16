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
        self.new_credential = credential('Drac','instagram','Alucard','vokeee')

    def test__init__(self):
        '''
        test if initialization of credential is done correctly done
        '''
        self.assertEqual(self.new_credential.user_name,'Drac')
        self.assertEqual(self.new_credential.user.media_name,'instagram')
        self.assertEqual(self.new_credential.user.account_name,'Alucard')
        self.assertEqual(self.new_credential.password,'vokeee')

    def test_save_credentials(self):
        '''
        check if password is saved in password array
        '''
        self.new_credential.save_credentials()
        reddit = password('vokee','reddit','dankmemmer','memememe')
        reddit.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

	def tearDown(self):
        '''
        this clears the credentials list after test
        '''
        credential.credentials_list = []
        User.user_list =[]

    def test_display_credentials(self):
        '''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
        self.new_credential.save_credentials()
        reddit = credential('vokee','reddit','dankmemmer','memememe')
        reddit.save_credentials()
        gmail = credential('ruoey','Gmail','vokee','draxx')
		gmail.save_credentials()
        self.assertEqual(len(credential.display_credentials(reddit.user_name), 2))

    def test_search(self):
        """
        check if the method returns the correct method
        """
        self.new_credential.save_credentials()
        reddit = credential('vokee','reddit','dankmemmer','memememe')
        reddit.save_credentials()
        credential_exists = credential.search('reddit')
        self.assertEqual(credential_exists,reddit)

    def test_copy_credential(self):
        """
        test if the credential is copied correctly
        """
        self.new_credential.save_credentials()
        reddit = credential('vokee','reddit','dankmemmer','memememe')
        reddit.save_credentials()
        find_credential = None
        for credential in credential.user_credential_list:
            find_credential = credential_search(credential.media_name)
            return pyperclip.copy(find_credential.credential)
        credential.copy_credential(self.new_credential.media_name)
        self.assertEqual('memememe',pyperclip.paste())

if __name__ == '__main__':
    unittest.main()