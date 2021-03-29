from system.menu import Menu

class UpdateDbTablesBody(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, api_data, DB):
        self.api_data = api_data
        self.db = DB

        self.error = ""


        Menu([[("Update table: {}".format(""))]], " MENU - {} ".format(str(self)))  # drow menu


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


    print(type([]))
