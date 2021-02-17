
class MainMenu:

    MENU_DICT = {1: "BOOSTERS" + 12*" ", 2: "CAPSULES" + 12*" ",
                 3: "MISSIONS" + 5*" "}

    def __init__(self):
        print("MENU >>>" + ((max(self.MENU_DICT)* 23) - 8) * "-")
        for key in self.MENU_DICT:
            print(str(key) + ": " + self.MENU_DICT[key], end="")
        print("")
        print((max(self.MENU_DICT)* 23) * "-")

class Menu(MainMenu):
    BOOSTERS_MENU_DICT = {11 : "STATUS", 12: "SERIAL"}
    CAPSULES_MENU_DICT = {21 : "STATUS", 22: "SERIAL"}
    MISSIONS_DICT = {31 : "PREVIOUSE", 32 : "FUTURE"}

    def __init__(self, state):
        if state == 0:
            Menu()
        elif state == 1:
            MainMenu()
            self.sub_menu(state, self.BOOSTERS_MENU_DICT)
        elif state == 2:
            MainMenu()
            self.sub_menu(state, self.CAPSULES_MENU_DICT)
        elif state == 3:
            MainMenu()
            self.sub_menu(state, self.MISSIONS_DICT)

    def sub_menu(self, state, dict):
        for key in dict:
            print((state -1)*23 * " " + "> " + str(key) + ": " + dict[key])
        print((max(self.MENU_DICT)* 23) * "-")


if __name__ == "__main__":
    m = Menu(3)
