from system.menu import Menu

class InsertDbTablesBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, api_data, DB):
        self.api_data = api_data
        self.db = DB
        columns = ""
        columns_data = ""

        Menu([[("{}".format("Update tables: "))]], " MENU - {} ".format(str(self)))  # drow menu



        # zamienić funkcjonalność z UPDATE !!!!



    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

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