
class UserStateSelection:
    def __init__(self, state):
        try:
            self.choice = int(input(">>> Put menu number: "))
        except ValueError:
            self.choice = state

    def return_state(self):
        return self.choice



