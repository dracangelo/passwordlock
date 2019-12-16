import pyperclip
import random
import string

#global variables

global user_list
class User:
    """
    generates a new user
    """
    pass
users_list = []

def __init__(self,first_name,last_name,password):
    """
    method defines the property for each object to hold
    """
    self.first_name = first_name
    self.last_name = last_name
    self.password = password

def save_user_details(self):
    """
    saves into user array
    """
    User.users_list.append(self)


class credential:
    """
    used to generate the credential
    """
    credentials_list = []
    user_credentials_list = []
    @classmethod
    def check_user(cls,first_name,password):
        '''
        checks if the name and password entered match the entries in the users list
        '''
        current_user = ''
        for user in users_list:
            if(user.first_name == first_name and user_password == password):
                current_user = user.first_name
        return current_user

