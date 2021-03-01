'''
file version 2.1
'''



import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from terminaltables import AsciiTable, SingleTable, DoubleTable


class Menu:

    def __init__(self, MENU_DICT):
        '''
            self.MENU_DICT = [
                            {1: "BOOSTERS", 2: "CAPSULES", 3: "MISSIONS"},
                            [{11: "STATUS", 12: "SERIAL"}, {21: "STATUS", 22: "SERIAL"}, {31: "PREVIOUSE", 32: "FUTURE"}],
                            [{111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"},
                           {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"},
                           {}]
                          ]
        '''

        self.MENU_DICT = MENU_DICT
        self.TABLE_DATA = []
        self.create_menu_table()

    def create_menu_table(self):
        for element in self.MENU_DICT:
            if isinstance(element, dict):
                self.TABLE_DATA.append(self.create_row_from_dict(element))
            elif isinstance(element, list):
                self.TABLE_DATA.append(self.create_row_from_list(element))

    def create_row_from_dict(self, dict):
        row = []
        for key in dict:
            row.append("{}: {}".format(key, dict[key]))
        return row

    def create_row_from_list(self, list):
        row = []
        column_in_row = ""
        for element in list:
            column_in_row = self.create_column_from_dict(element)
            row.append(column_in_row.rstrip("\n"))
        return row

    def create_column_from_dict(self, dict):
        column = ""
        for key in dict:
            column += str(key) + ": " + str(dict[key]) + "\n"
        return column

    def drow_menu(self):
        #menu = AsciiTable(self.table)
        #menu = SingleTable(self.table)
        menu = DoubleTable(self.TABLE_DATA, title = " MENU ")

        print(menu.table)

class SmartMenu(Menu):

    def cover_menu_by_state(self, state, table_size = [3, 2]):
        self.table_width = 70

        self.create_templane(table_size)

        #self.table[0] = self.TABLE_DATA[0]

        self.table[0][0] = self.TABLE_DATA[0][0] + (int(self.table_width / len(self.table[0]))
                                                    - len(self.TABLE_DATA[0][0])) * " "
        self.table[0][1] = self.TABLE_DATA[0][1] + (int(self.table_width / len(self.table[0]))
                                                    - len(self.TABLE_DATA[0][1])) * " "
        self.table[0][2] = self.TABLE_DATA[0][2] + (int(self.table_width / len(self.table[0]))
                                                    - len(self.TABLE_DATA[0][2])) * " "

        if state == 1 or (state > 100 and state < 120):

            self.table[1][0] = self.TABLE_DATA[1][0]
        elif state == 2 or (state > 200 and state < 220) :
            self.table[1][1] = self.TABLE_DATA[1][1]
        elif state == 3:
            self.table[1][2] = self.TABLE_DATA[1][2]

        if state == 11:
            self.table[1][0] = self.TABLE_DATA[2][0]
        elif state == 21:
            self.table[1][1] = self.TABLE_DATA[2][1]
        elif state == 31 or state == 32:
            self.table[1][2] = self.TABLE_DATA[1][2]

    def drow_menu(self):
        menu = DoubleTable(self.table, title = " MENU ")
        print(menu.table)

    def create_templane(self, table_size):
        self.table = []
        column = []
        for _ in range(table_size[1]):
            for _ in range(table_size[0]):
                column.append("")
            self.table.append(column)
            column = []


def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"
    # Action
    #return subprocess.call(command) == 0
    return os.system(command)



if __name__ == "__main__": # for tests

    HEADING_MENU_DICT = {1: "BOOSTERS", 2: "CAPSULES", 3: "MISSIONS"}
    BOOSTERS_MENU_DICT = {11 : "STATUS", 12: "SERIAL"}
    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_MENU_DICT = {21 : "STATUS", 22: "SERIAL"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}
    MISSIONS_DICT = {31 : "PREVIOUS", 32 : "FUTURE"}

    MENU_DICT = [
                HEADING_MENU_DICT,
                [BOOSTERS_MENU_DICT, CAPSULES_MENU_DICT, MISSIONS_DICT],
                [BOOSTERS_STATUS_DICT,CAPSULES_STATUS_DICT, {}]
                ]

    m = SmartMenu(MENU_DICT)
    m.cover_menu_by_state(1)
    m.drow_menu()