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



if __name__ == '__main__':
	main()