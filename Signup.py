"""
This is a module for signup
"""
from User import User

USER_LIST = []

new_name = input("Name: ")
new_username = input("Username: ")
new_email = input("Email: ")
new_password = input("Password: ")


def create_user():

    user = User(new_name, new_username, new_email, new_password)
    user.set_username(new_name)

    for man in USER_LIST:
         if self.name != user:
             USER_LIST.append(user)
         else:
             print("Enter real names")

create_user()
print(USER_LIST)