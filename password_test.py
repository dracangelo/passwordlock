import unittest
from password import Password

class testUser(unittest.TestCase):
    def setUp(self):
        """
        set up to run before each test case.

        """
        self.new_password = Password("user_name","password","email@ms.com") #this creates a new password

    def tearDown(self):
        """
        cleans up after each case has run
        """
        Password.Password_array = []

    def test_init(self):
        """
        test if objects are well initialized
        """
        self.assertEqual(self.new_password.user_name,"user_name")
        self.assertEqual(self.new_password.password,"password")
        self.assertEqual(self.new_password.email,"email@ms.com")

    def test_save_password(self):
        """
        test if the password is saved in array
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.Password_array),1)

    def test_display_password(self):
        """
        return a list of saved password
        """
        self.assertEqual(Password.display_password(),Password.Password_array)

if __name__ == '__main__':
    unittest.main()