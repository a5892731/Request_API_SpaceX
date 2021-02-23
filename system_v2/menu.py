'''
menu v 2.0
'''



import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from terminaltables import AsciiTable


class Menu:

    BOOSTERS_MENU_DICT = {11: "STATUS", 12: "SERIAL"}
    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}
    CAPSULES_MENU_DICT = {21: "STATUS", 22: "SERIAL"}
    MISSIONS_DICT = {31: "PREVIOUSE", 32: "FUTURE"}


    def __init__(self, status, MENU_DICT):
        '''
            self.MENU_DICT = [{1: "BOOSTERS", 2: "CAPSULES", 3: "MISSIONS"},
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

        self.cover_menu_by_status()

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
            for key in element:
                column_in_row += str(key) + ": " + str(element[key]) + "\n"
            row.append(column_in_row.rstrip("\n"))
            column_in_row = ""
        return row

    def drow_menu(self):
        menu = AsciiTable(self.TABLE_DATA)
        print(menu.table)

        print(self.TABLE_DATA)

    def cover_menu_by_status(self):

        if self.status > 10 and self.status < 100:
            self.MENU_DICT[2] = []

        if self.status == 0:
            self.MENU_DICT = [self.MENU_DICT[0]]

        elif self.status == 1:
            self.MENU_DICT[1][1] = []
            self.MENU_DICT[1][2] = []

        elif self.status == 2:
            self.MENU_DICT[1][0] = []
            self.MENU_DICT[1][2] = []

        elif self.status == 3:
            self.MENU_DICT[1][0] = []
            self.MENU_DICT[1][1] = []

        elif self.status > 10 and self.status < 20:
            self.MENU_DICT[1][0] = self.MENU_DICT[2][0]
            self.MENU_DICT[1][1] = []
            self.MENU_DICT[1][2] = []

        elif self.status > 20 and self.status < 30:
            self.MENU_DICT[1][0] = []
            self.MENU_DICT[1][1] = self.MENU_DICT[2][1]
            self.MENU_DICT[1][2] = []

        elif self.status > 30 and self.status < 40:
            self.MENU_DICT[1][0] = []
            self.MENU_DICT[1][1] = []
            self.MENU_DICT[1][2] = self.MENU_DICT[2][2]

        if self.status > 0 and self.status < 100:
            self.MENU_DICT[2] = []


def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"
    # Action
    #return subprocess.call(command) == 0
    return os.system(command)



if __name__ == "__main__": # test

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

    m = Menu(21, MENU_DICT)
    m.drow_menu()