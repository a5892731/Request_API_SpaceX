from system.menu import Menu

class ReadDbTablesLenBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, api_data, DB):
        self.api_data = api_data
        self.db = DB
        self.db_sizes = {}
        self.error = ""

        progres_bar = 0
        for key in api_data:

            query = "SELECT table_id FROM {} ORDER BY table_id DESC LIMIT 0 , 1".format(key.lower())
            progres_bar += 1
            response = self.db.execute_read_query(self.db.connection, query,
                                                   "Loading tables length: {} %".format(int((progres_bar/len(api_data) * 100))))
            size_of_database = 0
            if response != []:
                size_of_database = response[0][0]
            self.db_sizes[key] = size_of_database

            Menu([[("{}".format(self.db.status))]]," MENU - {} ".format(str(self)))  # drow menu

            if "error" in self.db.status:
                self.error += self.db.status + "\n"
        #----------------------------------------------------------------------------------------------------------------

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

