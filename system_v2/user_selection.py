'''
file version 1.1
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
    def __init__(self, string):
        self.serial = input(string)
    def return_serial(self):
        return self.serial