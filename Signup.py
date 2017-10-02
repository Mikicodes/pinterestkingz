from datetime import datetime
import os.path
import csv

from User import User

"""

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
"""


class Users:

    def __init__(self, users = []):
        self.users = users


    def user_list(self, user):
        self.users.append(user)

    def create_csv(self, user):

        file_exist = os.path.isfile('user.csv')
        with open('user.csv', 'a') as csv_file:
            fieldnames = ['firstname', 'lastname', 'email', 'password', 'birthday', 'gender']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow(
                {'firstname': user.firstname, 'lastname': user.lastname, 'email': user.email, 'password': user.password, 'birthday': user.birthday, 'gender': user.gender})