'''
here are the rules of state transition
'''

from state_machine.states.initialization import InitializationBody
from state_machine.states.get_connection_data import GetConnectionDataBody
from state_machine.states.get_api import GetDataFromApiBody
from state_machine.states.user_choice import UserChoiceBody
from state_machine.states.error import ErrorBody


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

        if event == 'device_locked' and self.request_status == 200:
            return UserChoice(self.api_data)
        elif event == 'device_locked' and self.request_status != 200:
            return Error(self.error)
        return self

class UserChoice(UserChoiceBody):
    def on_event(self, event):

        if event == 'device_locked':
            return Initialization()
        return self

class Error(ErrorBody):
    def on_event(self, event):
        return Error(self.error)