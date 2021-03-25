from system.menu import Menu

class InitializationBody(object):

    def __init__(self):

        Menu([["START PROGRAM".center(68)]], " MENU - {} ".format(str(self)))

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
