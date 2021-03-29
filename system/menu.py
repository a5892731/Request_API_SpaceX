'''
author: a5892731
date: 2021-03-22
'''



import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from terminaltables import AsciiTable, SingleTable, DoubleTable


class Menu:
    version = "1.0"
    menu_width = 69

    def __init__(self, table_menu, menu_title = " MENU "):
        self.table_menu = table_menu
        self.table_to_print = []
        self.prepare_table()

        self.clear_screen()
        self.drow_menu(menu_title)

    def prepare_table(self):

        num_of_columns= len(self.table_menu[0])
        column_width = int((self.menu_width - 2 * num_of_columns + 2 ) / num_of_columns)


        for row in self.table_menu:
            row_table = []
            for column in row:
                lines = []
                if len(column) < column_width:
                    row_table.append(str(column) + " " * (column_width - int(len(column))))
                elif len(column) == column_width:
                    row_table.append(str(column))
                else:
                    new_column = ""
                    for word in column.split():
                        if (len(new_column) + len(word)) < column_width:
                            new_column += word + " "
                        else:
                            if len(word) > column_width:
                                en_of_word = (column_width - len(new_column) - 1)
                                new_column += word[0: en_of_word] + "-"
                                lines.append(new_column)
                                new_column = word[en_of_word:]

                            else:
                                new_column += " " * (column_width - len(new_column))
                                lines.append(new_column)
                                new_column = word + " "
                    lines.append(new_column)
                    column = ""
                    for line in lines:
                        column += str(line) + "\n"
                    row_table.append(column.rstrip("\n"))
            self.table_to_print.append(row_table)

    def drow_menu(self, menu_title = " MENU "):
        menu = DoubleTable(self.table_to_print, title = menu_title)
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

        return output



if __name__ == "__main__": # for tests

    MENU = [["testdddddddddddddddddddddXXdddddX ", "test", "test"], ["tesest sdaaaaa adssssss", "test", "test"], ]
    m = Menu(MENU, " title ")


    MENU = [["123456789012345678901234567890123456789", "test", "test"]]
    m = Menu(MENU, " title ")


    MENU = [["testdddd sadada sdada a sa asd  as add ", "test", "test"]]
    m = Menu(MENU, " title ")


    MENU = [[""]]
    m = Menu(MENU, " title ")


    MENU = [["", ""]]
    m = Menu(MENU, " title ")


    MENU = [["", "", "", ""]]
    m = Menu(MENU, " title ")


    MENU = [["Zadaniem programisty bardzo często jest obsługa zmiennych napisowych (łańcuchów znaków) czyli tzw. stringów. Dzieje się to szczególnie często w przypadku programowania webowego. Zagadnienie zmiennych napisowych w Pythonie jest wbrew pozorom bardzo obszerne. W tym artykule chciałbym skupić się na pokazaniu najpotrzebniejszych operacji związanych ze zmiennymi napisowymi."]]
    m = Menu(MENU, " title ")
    m.table_menu = [["", "", "", ""]]
    m.table_to_print = []
    m.prepare_table()
    m.drow_menu()
