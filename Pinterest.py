from User import User
from Pin import Pin
from Board import Board
from datetime import datetime
import os.path
import csv



class Pinterest:

    # def __init__(self):
    user_list = []
    user_match = -1

    @staticmethod
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
        Pinterest.user_list.append(user)
        print("You have Signed Up")

        file_exist = os.path.isfile('user.csv')
        with open('user.csv', 'a') as csv_file:
            fieldnames = ['username','password']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'username': user.get_name(), 'password': user.get_password()})


    @staticmethod
    def signin():
        """
        this asks for two parameters to check users in the csv file

        """
        ask_name = input("Your username? ")
        ask_password = input("Password: ")

        with open("user.csv", 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            # this checks and loops thru the reader dictionary
            Pinterest.user_match = False
            for read in reader:
                if ask_name == read['username'] and ask_password == read['password']:
                    Pinterest.user_match = True

                    #setting the user to be operated on as soon as signin is complete
                    for user in Pinterest.user_list:
                        if user.get_name() == ask_name:
                            present_user = user

            # this prints the output if the user is found
            if Pinterest.user_match:
                print('Welcome ', ask_name.capitalize())


            else:
                print('Sorry your password and username don\'t match')



    #View the Homepage
    def homepage(self):
        #
    	for user in USER_LIST:
    		for board in user.boards:
    			return board.pins
    

    #Loop the things
    def call(self):

        run = True
        while run == True:
            choice = input("What do you want to do?\n1 Sign in\n2 Sign up\n3 Exit")

            if choice == "1":
                Pinterest.signin()
                while Pinterest.user_match == True:
                    activities = int(input("Create pin or board? \n1 - Pin \n2 - Board"))

                    if activities == 1:
                        present_user.create_pin()
                    
                    elif activities == 2:
                        # user create boards
                        present_user.create_board()
                    else:
                        print("Have a good day!")


            if choice == "2":
                Pinterest.signup()

            if choice == "3":
                print("Goodbye!")
                run = False

start = Pinterest()
start.call()