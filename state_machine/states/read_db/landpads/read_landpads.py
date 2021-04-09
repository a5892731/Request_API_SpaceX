from system.read_data_files import DataImport
from state_machine.states.read_db.read_database import ReadDbBody
import os
from system.menu import Menu

class LandpadsBody(ReadDbBody):

    def __init__(self):

        self.table = "landpads"
        self.error = ""
        self.all_data()


    def all_data(self):
        data_view_limit = 1


        self.connection_to_db()
        column_list = DataImport("ALL_DATA_COLUMN_LIST.txt", "list", "db_configuration/{}".format(self.table))
        os.chdir("..")
        query = DataImport("ALL_DATA_QUERY.txt", "string", "db_configuration/{}".format(self.table))
        os.chdir("..")

        self.connection_to_db()
        self.query = query()

        response = self.send_sql_query(self.query)
        self.read_sql_response(response, self.table, column_list(), data_view_limit) # read and print in console






if __name__ == "__main__":

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


    test = LandpadsBody()




    os.chdir("state_machine")
    os.chdir("states")
    os.chdir("read_db")
    os.chdir("boosters")