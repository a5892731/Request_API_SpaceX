import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os

class MainMenu:

    MENU_DICT = {1: "BOOSTERS" + 12*" ", 2: "CAPSULES" + 12*" ",
                 3: "MISSIONS" + 5*" "}

    def __init__(self):
        print("\n" + (max(self.MENU_DICT)* 23) * "-")
        for key in self.MENU_DICT:
            print(str(key) + ": " + self.MENU_DICT[key], end="")
        print("")
        print((max(self.MENU_DICT)* 23) * "-")

class Menu(MainMenu):
    BOOSTERS_MENU_DICT = {11 : "STATUS", 12: "SERIAL"}
    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}
    CAPSULES_MENU_DICT = {21 : "STATUS", 22: "SERIAL"}
    MISSIONS_DICT = {31 : "PREVIOUSE", 32 : "FUTURE"}

    def __init__(self, state):

        if state == 1:
            MainMenu()
            self.sub_menu(state, self.BOOSTERS_MENU_DICT)
        elif state == 11:
            MainMenu()
            self.sub_menu(state - 10, self.BOOSTERS_MENU_DICT)
            self.sub_menu(state - 10, self.BOOSTERS_STATUS_DICT, 2)
        elif state == 2:
            MainMenu()
            self.sub_menu(state, self.CAPSULES_MENU_DICT)
        elif state == 21:
            MainMenu()
            self.sub_menu(state - 20 + 1, self.CAPSULES_MENU_DICT)
            self.sub_menu(state - 20 + 1, self.CAPSULES_STATUS_DICT, 2)

        elif state == 3:
            MainMenu()
            self.sub_menu(state, self.MISSIONS_DICT)
        else:
            MainMenu()

    def sub_menu(self, state, dict, deeph = 1):
        for key in dict:
            print((state -1)*23 * " " + ">" * deeph + " " + str(key) + ": " + dict[key])
        print((max(self.MENU_DICT)* 23) * "-")

def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"
    # Action
    #return subprocess.call(command) == 0
    return os.system(command)



if __name__ == "__main__":
    m = Menu(3)
