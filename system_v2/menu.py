'''
menu v 2.0
'''



import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from terminaltables import AsciiTable, SingleTable, DoubleTable


class Menu:

    def __init__(self, status, MENU_DICT):
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
        self.status = status
        self.TABLE_DATA = []
        self.table = [
                      ["", "", ""],
                      ["", "", ""]
                     ]

        for element in self.MENU_DICT:
            if isinstance(element, dict):
                self.TABLE_DATA.append(self.create_row_from_dict(element))
            elif isinstance(element, list):
                self.TABLE_DATA.append(self.create_row_from_list(element))

        self.cover_menu_by_status()

    def create_row_from_dict(self, dict):
        row = []
        for key in dict:
            row.append("{}: {}".format(key, dict[key]))
        return row

    def create_column_from_dict(self, dict):
        column = ""
        for key in dict:
            column += str(key) + ": " + str(dict[key]) + "\n"
        return column

    def create_row_from_list(self, list):
        row = []
        column_in_row = ""
        for element in list:
            column_in_row = self.create_column_from_dict(element)
            row.append(column_in_row.rstrip("\n"))
        return row

    def drow_menu(self):
        #menu = AsciiTable(self.table)
        #menu = SingleTable(self.table)
        menu = DoubleTable(self.table)

        print(menu.table)

        #print(self.TABLE_DATA[0][1])

    def cover_menu_by_status(self):

        self.table[0] = self.TABLE_DATA[0]

        if self.status == 1 or (self.status > 100 and self.status < 120):
            self.table[1][0] = self.TABLE_DATA[1][0]
        elif self.status == 2 or (self.status > 200 and self.status < 220) :
            self.table[1][1] = self.TABLE_DATA[1][1]
        elif self.status == 3:
            self.table[1][2] = self.TABLE_DATA[1][2]

        if self.status == 11:
            self.table[1][0] = self.TABLE_DATA[2][0]
        elif self.status == 21:
            self.table[1][1] = self.TABLE_DATA[2][1]



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

    m = Menu(1, MENU_DICT)
    m.drow_menu()