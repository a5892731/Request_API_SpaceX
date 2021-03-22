from system.menu import Menu
from time import sleep


class ErrorBody(object):

    def __init__(self, error):
        self.error = error

        Menu([[self.error.center(68)]], " MENU - {} ".format(str(self)))


    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__

    def print_menu(self, menu_list):
        menu = Menu(menu_list)
        menu.drow_menu(" MENU - " + str(self) + " ")
        sleep(1)