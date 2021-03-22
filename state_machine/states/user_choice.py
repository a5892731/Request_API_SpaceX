from system.menu import Menu

class UserChoiceBody(object):

    def __init__(self):

        menu_list = [["1: Update Database", "2: Read Database", "5: Settings", "4: Close Program"]]
        menu = Menu(menu_list)
        menu.drow_menu(" MENU - " + str(self) + " ")
        self.choice = input(">>> Enter menu number: ")
        menu.clear_screen()

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

