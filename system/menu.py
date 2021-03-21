'''
author: a5892731
date: 2021-03-21
'''



import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from terminaltables import AsciiTable, SingleTable, DoubleTable


class Menu:
    version = "1.0"

    def __init__(self, table_menu):

        self.table_menu = table_menu



    def drow_menu(self, menu_title = " MENU "):
        #menu = AsciiTable(self.table)
        #menu = SingleTable(self.table)
        menu = DoubleTable(self.table_menu, title = menu_title)

        print(menu.table)

    def clear_screen(self):
        """
        Clears the terminal screen.
        """
        # Clear command as function of OS
        command = "cls" if platform.system().lower() == "windows" else "clear"
        # Action
        # return subprocess.call(command) == 0
        return os.system(command)





if __name__ == "__main__": # for tests

    MENU = [["test", "test", "test"], ["test", "test", "test"], ]


    m = Menu(MENU)
    m.drow_menu()