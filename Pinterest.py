from User import User
from Pin import Pin
from Board import Board
from Signout import Signout
from Signup import Signup
from datetime import datetime
import os.path
import csv


user_list = []

def signup():

    user = User()
    new_name = input("Name: ")
    new_username = input("Username: ")
    new_email = input("Email: ")
    new_password = input("Password: ")
    user.set_name(new_name)
    user.set_username(new_username)
    user.set_email(new_email)
    user.set_password(new_password)
    user_list.append(user)

    file_exist = os.path.isfile('user.csv')
    with open('user.csv', 'a') as csv_file:
        fieldnames = ['username','password']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exist:
            writer.writeheader()
        writer.writerow({'username': user.get_name(), 'password': user.get_password()})


def signin():
    """
    this asks for two parameters to check users in the csv file

    """
    ask_name = input("Your username? ")
    ask_password = input("Password: ")

    with open("user.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # this checks and loops thru the reader dictionary
        user_match = False
        for read in reader:
            if ask_name == read['username'] and ask_password == read['password']:
                user_match = True

        # this prints the output if the user is found
        if user_match:
            print('Welcome ', ask_name.capitalize())
        else:
            print('Sorry your password and username don\'t match')


def homepage():
	for user in USER_LIST:
		for board in user.boards:
			return board.pins

signup()