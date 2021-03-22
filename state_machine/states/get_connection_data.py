from system.menu import Menu
#from system.db import Database


class GetConnectionDataBody(object):

    def __init__(self):
        menu_list = [[""]]
        self.print_menu(menu_list)

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
        menu.clear_screen()