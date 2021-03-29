from system.menu import Menu
from subprocess import Popen


class InitializationBody(object):

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """

        #Popen(["mode", "con:", "cols=25", "lines=80"])
        Menu([[("Start program")]], " MENU - {} ".format(str(self)))  # drow menu


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
