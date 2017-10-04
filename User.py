from datetime import datetime
from Board import Board
from Pin import Pin

class User(object):
    """Constructor of the user"""
    def __init__(self):
        self.followers = []
        self.following = []
        # self.profile_picture = profile_picture
        self.boards = []
        self.signin_state = False
        self.interest_list = []
    #Ressign a name to the User
    def set_name(self,name):
        self.name = name

    #Return name of the User
    def get_name(self):
        return self.name

    #Reasign a username to User
    def set_username(self,username):
        self.username = username

    #Return username of the User
    def get_username(self):
        return self.username
    
    #Reassign the email of the User
    def set_email(self,email):
        self.email =email

    #Return the email of the User
    def get_email(self):
        return self.email

    #Reassign the password of the User
    def set_password(self, password):
        self.password = password

    #Return the password of the User
    def get_password(self):
        return self.password

    #Reasign an interest to User
    def set_interest(self,interest):
        self.interest_list.append(interest)

    #Return interest of the User
    def get_interest(self):
        return self.interest_list

    #Reasign a country to User
    def set_country(self,country):
        self.country = country

    #Return country of the User
    def get_country(self):
        return self.country

    #Reasign a about_info to User
    def set_about_info(self,about_info):
        self.about_info = about_info

    #Return about_info of the User
    def get_about_info(self):
        return self.about_info

    #Reasign a current_location of User
    def set_current_location(self,current_location):
        self.current_location = current_location

    #Return current_location of the User
    def get_current_location(self):
        return self.current_location

    #Reasign a registration_date to User
    def set_registration_date(self,registration_date):
        self.registration_date = datetime.now()

    #Return registration_date of the User
    def get_registration_date(self):
        return self.registration_date

    #Reasign a followers to User
    def set_followers(self,follower):
        self.followers.append(follower)

    #Return followers of the User
    def get_followers(self):
        return self.followers

    #Reasign a following to User
    def set_following(self,following):
        self.following = following

    #Return following of the User
    def get_following(self):
        return self.following

    #Reasign a profile_pic to User
    def set_profile_pic(self,profile_pic):
        self.profile_pic = profile_pic

    #Return create board of the User
    def get_profile_pic(self):
        return self.profile_pic

    #Create a Board for the specific User
    def create_board(self):
        board = Board()
        board.set_name(input("Enter Board Name:"))
        board.set_category(input("Enter Board Category:"))
        board.set_description(input("Enter Board Description:"))
        self.boards.append(board)

    #Create a pin and place it in a Board
    def create_pin(self):
        pin = Pin()
        pin.set_name(input("Enter pin name:"))
        pin.set_description(input("Enter pin description:"))
        pin.set_picture(input("Enter picture:"))
        board_c_status = input("To add to Existing board, enter 1 ; 2 to create board:")

        if int(board_c_status) == 1:
            board_add = input("Enter the name of existing Board:")
            for board in self.boards:
                if board.get_name() == board_add:
                    board.add_pins(pin)
                    print("Pin added to Board {}".format(board.get_name()))
                else:
                    print("Board does not exist")

        elif int(board_c_status) == 2:
            board = Board()
            board.set_name(input("Enter Board Name:"))
            board.set_category(input("Enter Board Category:"))
            board.set_description(input("Enter Board Description:"))
            board.add_pins(pin)
            print("Board {} created and Pin {} added".format(board.get_name(), pin.get_name()))

        else:
            print("Wrong option")

user = User()
user.create_board()
user.create_pin()

