#! /usr/bin/env python3.6
import pyperclip
from user import User

def create_user(first_name, last_name, password):
    """
    this creates a new account user
    """
    create_user = User(first_name,last_name,password)
    return create_user

def save_user(user):
    '''
    this saves a new user
    '''
    User.save_user
    
def check_user(first_name,password)
    """
    checks existence of a user before creating credentials
    """
    verify_user = Credential.veryfy_user(first_name,password)
    return verify_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,media_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,media_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def copy_credential(media_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(media_name)
if __name__ == '__main__':
	main()