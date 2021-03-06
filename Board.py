import datetime
from Pin import Pin


class Board:

    def __init__(self):
        # initializing the class, these are the attributes to appear at initialization
        self.pins = list()

    def set_name(self, name):
        # setting the name of the board
        self.name = name
        
    def get_name(self):
        # returning the set name of the board
        return self.name

    def add_pins(self, pin):
        # creating a list of pins to appear in the board
        self.pins.append(pin)

    def get_pins(self):
        # returning the list of pins
        return self.pins

    def set_category(self, category):
        # assigning a category to the board'
        self.category = category

    def get_category(self):
        # returning the category of the board
        return self.category

    def set_description(self, description):
        # allows the user to add a description for a board
        self.description = description

    def get_description(self):
        # returning the description of the board
        return self.description

    def set_collaborators(self, collaborator):
        # creating a list of collaborators
        self.collaborator = list(collaborator)

    def get_collaborators(self):
        # returning the list of collaborators
        return self.collaborator

    def set_date_time(self):
        # setting the date and time of creation of a board
        self.date = datetime.datetime.now().date()
        self.time = datetime.datetime.now().time()

    def get_date_time(self):
        # returning the date and time of creation of the board
        return print('Created on {} at {}'.format(self.date, self.time))