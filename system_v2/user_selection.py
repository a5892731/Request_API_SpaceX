'''
version 1.0
'''


class UserStateSelection:
    def __init__(self, state):
        try:
            self.choice = int(input(">>> Put menu number: "))
        except ValueError:
            self.choice = state

    def return_state(self):
        return self.choice



class UserSerialSelection:
    def __init__(self):
        self.serial = input(">>> Put vehicle serial number: ")
    def return_serial(self):
        return self.serial