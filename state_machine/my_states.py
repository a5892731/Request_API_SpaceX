'''
here are the rules of state transition
'''

from state_machine.states.initialization import InitializationBody
from state_machine.states.get_connection_data import GetConnectionDataBody
from state_machine.states.get_api import GetDataFromApiBody

from state_machine.states.user_choice import UserChoiceBody



# Start of our states <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Initialization(InitializationBody):
    def on_event(self, event):

        if event == 'device_locked':
            return GetConnectionData()
        return self

class GetConnectionData(GetConnectionDataBody):
    def on_event(self, event):

        if event == 'device_locked':
            return GetDataFromApi()
        return self

class GetDataFromApi(GetDataFromApiBody):
    def on_event(self, event):
        print(self.api_data)


        if event == 'device_locked':
            return UserChoice()
        return self

class UserChoice(UserChoiceBody):
    def on_event(self, event):

        if event == 'device_locked':
            return Initialization()
        return self