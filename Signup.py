"""
This is a module for signup
"""

class Signup:
    """
    This class requires the user to enter the name, password, email
    """

    # This is a list of users that sign up on the app

    USER_LIST = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def create_user(self):
        temp_user = User()
        temp_user.set_username("kelvin")
        temp_user
        # for user in USER_LIST:
        #      if self.name != user:
        #          USER_LIST.append()