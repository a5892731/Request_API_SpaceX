from system.menu import Menu

class InitializationBody(object):

    def __init__(self):

        menu_list = [[70 * " "]]
        self.print_menu(menu_list)

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

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