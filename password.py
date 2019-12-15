class Password:
    """
    helps generate a credential for a new user
    """

    pass
    Password_array = []

    def __init__(self, user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_password(self):
        """
        save password in password array
        """
        Password.Password_array.append(self)

    @classmethod
    def display_password(cls):
        return cls.Password_array


