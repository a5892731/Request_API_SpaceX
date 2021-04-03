from system.menu import Menu
from system.db import Database
from system.read_data_files import DataImport
import os

class ReadDbBody(object):

    def __init__(self):

        menu_dict = {"1": "Launches", "2": "Boosters", "3": "Capsules", "4": "Rockets",
                     "5": "Crew", "6": "Payloads", "7": "Ships", "8": "Launchpads",
                     "9": "Landpads", "10": "Main Menu",}


        menu_list = [["Menu list:"]]

        for key in menu_dict:
            menu_list.append([key + ": " + menu_dict[key]])

        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")
        self.error = ""
        self.table = ""


    def on_user_choice(self):
        self.connection_to_db()
        self.choice = ""


    def connection_to_db(self):
        Menu([["Connecting ..."]], " MENU - {} ".format(str(self)))  # drow menu

        connection_parameters = DataImport("CONNECTION_DATA.txt", "dict", "db_configuration")
        tables = DataImport("TABLES.txt", "dict", "db_configuration")
        # ----------------------------------------------------------------------------CONNECTION---------------------

        self.db = Database(connection_parameters()["database"], connection_parameters()["host"],
                            connection_parameters()["user"], "", tables())  # connection_parameters()["password"]
        try:
            self.db.connection = self.db.create_connection_to_db("")  # connection_parameters()["password"]
        except AttributeError:
            self.error = "Error: cant find database"

        if "error" in self.db.status:
            self.error += self.db.status + "\n"
        # -----------------------------------------------------------------------------------------------------------

    def read_from_table(self, table, column_list, selected_column_name = "", selected_column_value = "", order = "", order_type = "", data_view_limit = 5):
        '''
        :param table: table name
        :param column_list: list of columns to print
        :param selected_column_name: by this column you will sort table
        :param selected_column_value: if order = "ORDER" it must be empty
        :param order: order = "ORDER" or "". order or selected_column_value must be empty
        :param order_type: if order == "ORDER" then it shauld have a type "ASC" or "DESC"
        :param data_view_limit: limit how many tables you want to print in console (max)
        :return: print server data
        '''
        self.table = table
        query = ""
        column_names = ""

        for column in column_list:
            column_names += column + ", "
        column_names = column_names.rstrip(", ")

        if selected_column_value != "":
            selected_column_value = "= '" + selected_column_value + "'"
            query_command_list = ("SELECT", column_names, "FROM", table, "WHERE", selected_column_name, selected_column_value)
        else:
            query_command_list = ("SELECT", column_names, "FROM", table, order, "BY", selected_column_name, order_type)

        for command in query_command_list:
            if command != "":
                query += command + " "
            query.rstrip(" ")

        #print(query)
        response = self.send_sql_query(query)
        self.read_sql_response(response, table, column_list, data_view_limit) # read and print in console

    def read_from_many_tables(self, table_list, column_list_list, relations_dict, order = "", order_type = "DESC", data_view_limit = 5):

        query = ""
        column_names = ""
        tables = ""
        relations = ""
        new_column_list = []

        for number in range(len(table_list)):
            tables += table_list[number] + ", "
            for column in column_list_list[number]:
                column_names += table_list[number] + "." + column + ", "
                if number == 0:
                    new_column_list.append(column)
                else:
                    new_column_list.append(table_list[number] + " " + column)

        column_names = column_names.rstrip(", ")
        tables = tables.rstrip(", ")


        for key in relations_dict:
            relations = str(key) + " = " + str(relations_dict[key]) + " AND "
        relations = relations.rstrip(" AND ")


        if order == "":
            query_command_list = ("SELECT", column_names, "FROM", tables, "WHERE", relations)
        else:
            query_command_list = ("SELECT", column_names, "FROM", tables, "WHERE", relations, "ORDER BY", order, order_type)

        for command in query_command_list:
            if command != "":
                query += command + " "
            query.rstrip(" ")

        response = self.send_sql_query(query)
        self.read_sql_response(response, table_list[0], new_column_list, data_view_limit)  # read and print in console


    def send_sql_query(self, query):
        '''
        :param query:
        query = SELECT columns FROM table BY column_name = column_value
        query = SELECT columns FROM table order BY column_name desc
        query = SELECT columns FROM table

        :return: server response
        '''
        response = self.db.execute_read_query(self.db.connection, query, "Read {} table completed".format(self.table))
        Menu([[self.db.status]], " MENU - {} ".format(str(self)))  # drow menu
        if "error" in self.db.status:
            self.error += self.db.status + "\n"
        return response



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


    def all_data_from_many(self, menu_dict, table_list, column_list_list, relations_dict, order_type = "DESC"):

        menu_list = [[key + ": " + menu_dict[key] for key in menu_dict]]

        Menu(menu_list, " MENU - {} ".format(str(self)))
        self.choice = input(">>> Enter menu number: ")

        try:
            if "Sort" in menu_dict[self.choice]:
                order_by = table_list[0] + "." + menu_dict[self.choice][8:]

                self.read_from_many_tables(table_list, column_list_list, relations_dict, order_by, "DESC")
        except KeyError:
            pass


    def by_column_value(self, column = "", value = ""):
        '''
        :param column: sugestions: serial, flight_number, status, id
        :param value:
        :return:  print tables in console
        '''
        columns = DataImport("SELECT_{}.txt".format(self.table.upper()), "list", "db_configuration")
        self.read_from_table(self.table, columns(), column, value)




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


if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    test_number = 2

    test = ReadDbBody()
    test.on_user_choice()


    if test.error == "" and test_number == 1:
        table = "boosters"
        columns = DataImport("SELECT_{}.txt".format(table.upper()), "list", "db_configuration")


        test.read_from_table(table, columns(), "status", "active")


        test.read_from_table(table, columns(), "serial", "B1051")


        test.read_from_table(table, columns(), "serial", "wrong data") # no error, but empty data


        test.read_from_table(table, columns(), "table_id", "", "ORDER", "DESC")


        test.read_from_table(table, columns())  # error :)


        test.read_from_table(table, columns(), "wrong data", "1")  # error :)


    elif test.error == "" and test_number == 2:
        table1 = "launches"
        table2 = "launchpads"


        booster_columns = DataImport("SELECT_{}.txt".format(table1.upper()), "list", "db_configuration")

        # read_from_many_tables(self, table_list, column_list_list, relations_dict, order="", order_type="DESC", data_view_limit=5):


        test.read_from_many_tables([table1, table2],
                                   [booster_columns(), ["full_name"]],
                                   {"launches.launchpad": "launchpads.id"},
                                   "launches.flight_number", "DESC")



    os.chdir("state_machine")
    os.chdir("states")
