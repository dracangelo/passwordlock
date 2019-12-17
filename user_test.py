import unittest ##import unittest module
from user import User ##import user class from user.py file
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = User("mary","mbugua","nish","0789755096","mary@gmail.com","lovepy") #create user object
    def tearDown(self):
        '''
        cleans up after each test case has 
        been executed
        '''
        User.user_list = []
    def test_init(self):
        '''
        to test if object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name,"mary")
        self.assertEqual(self.new_user.last_name,"mbugua")
        self.assertEqual(self.new_user.user_name,"nish")
        self.assertEqual(self.new_user.phone_number,"0789755096")
        self.assertEqual(self.new_user.email,"mary@gmail.com")
        self.assertEqual(self.new_user.password,"lovepy") 
    def test_save_user(self):
        """
         to test if user object is saved
         into user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_save_multipleuser(self):
        """
         to test if we can save multiple users
         to the user list
        """
        self.new_user.save_user()
        test_user = User("testfirst","testlast","testusername","0712345678","test@user.com","testpassword")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_display_allusers(self):
        """
        test for method that returns
        all users saved
        """
        self.assertEqual(User.display_allusers(),User.user_list) 
    def test_generate_randompass(self):
        """
         test for method that generates a random password
         and returns a string
        """

        self.new_user.save_user()
        test_user = User("testfirst","testlast","testusername","0712345678","test@user.com","testpassword")
        test_user.save_user()
        randompass_generated = User.generate_randompass()
        self.assertEqual(str(randompass_generated),str(randompass_generated))

if __name__ == '__main__':
    unittest.main()
