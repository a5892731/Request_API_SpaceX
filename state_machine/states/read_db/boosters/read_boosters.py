from system.menu import Menu
from state_machine.states.read_db.read_database import ReadDbBody
from system.read_data_files import DataImport

import os

class BoostersBody(ReadDbBody):

    def __init__(self):

        self.error = ""
        self.table = "boosters"
        self.choice = ""

        select = DataImport("SELECT_BOOSTERS.txt", "string", "db_configuration")
        self.select = select()
        self.initialization()

    def initialization(self):
        menu_dict = {"1": "All data", "2": "By serial", "3": "By status", "4": "Go Back"}
        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]
        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        if self.choice == "1" and self.error == "":
            self.all_data()
        elif self.choice == "2" and self.error == "":
            self.by_serial()
        elif self.choice == "3" and self.error == "":
            self.by_status()
        elif self.go_back == "4" and self.error == "":
            self.by_status()
        else:
            pass

    def all_data(self):
        self.connection_to_db()






        self.query = "SELECT boosters.serial, launches.flight_number FROM boosters INNER JOIN launches ON boosters.launches LIKE CONCAT_WS('', '%', launches.id, '%')"

        pass

    def by_serial(self):
        self.connection_to_db()
        pass

    def by_status(self):
        self.connection_to_db()
        pass

    def go_back(self):
        self.initialization(self)


    def read_db(self, query, table, column_list, data_view_limit):
        response = self.send_sql_query(query)
        self.read_sql_response(response, table, column_list, data_view_limit) # read and print in console


    def read_sql_response(self, response, table, columns, data_view_limit = 5):
        def print_data_and_wait(menu):
            m = Menu(menu, " MENU - {} ".format(str(self)))  # drow menu
            m.__del__()
            return input("Continue? Y/N: ")

        menu = [[table.capitalize() + " data:"]]
        counter = 0
        if response != None:
            for row in response:
                counter += 1
                for column_number in range(len(row)):

                    if str(row[column_number]) != "[]" and str(row[column_number]) != "None":
                        menu_segment = columns[column_number] + ": " + str(row[column_number])
                        menu.append([menu_segment])
                menu.append(["-" * Menu.menu_width])

                if counter >= data_view_limit:
                    self.choice = print_data_and_wait(menu)
                    if self.choice.upper() == "N":
                        counter = 0
                        break
                    menu = [[table.capitalize() + " data:"]]
                    counter = 0
            if counter > 0:
                self.choice = print_data_and_wait(menu)
        else:
            self.error += "None type object in response\n"










if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


    test = BoostersBody()





    os.chdir("state_machine")
    os.chdir("states")
    os.chdir("read_db")
    os.chdir("boosters")