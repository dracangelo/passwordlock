import pyperclip
import random
import string

# Global Variables
global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)
		
class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user
        
    def __init__(self,user_name,media_name,account_name,password):
        """
        Method to define the properties for each user object will hold.
		""" 

		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
        self.password = password
        
    def save_credentials()
        '''
        save new users
        '''
        Credential.credentials_list.append(self)
        
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
        generate an 8 character password for password
        '''
        gen_pass = ''.join(rndom.choice(char) for _ in range(size))
        return gen_pass
    
    @classmethod
    def display_credentials(cls,user_name):
        '''
        display list of saved credentials
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
            return user_credentials_list
        
    @classmethod
    def search(cls, media_name):
        """
        takes in a media_name and returns the site credentials
        """
        for Credential in cls.credentials_list:
            if credential.media_name == media_name:
                return Credential
            
    @classmethod
    def copy_credential(cls, media_name):
        '''
		Class method that copies a credential's info after the credential's site name is entered
		'''
        find_credential = Credential.search(media_name)
        return pyperclip.copy(find_credential.password)