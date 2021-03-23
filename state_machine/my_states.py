'''
here are the rules of state transition
'''

from state_machine.states.initialization import InitializationBody
from state_machine.states.get_connection_data import GetConnectionDataBody
from state_machine.states.get_api import GetDataFromApiBody
from state_machine.states.user_choice import UserChoiceBody
from state_machine.states.error import ErrorBody
from state_machine.states.insert_db_tables import InsertDbTablesBody
from state_machine.states.update_db_tables import UpdateDbTablesBody
# Start of our states <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



class Initialization(InitializationBody):
    def on_event(self, event):

        if event == 'device_locked':
            return UserChoice()
        return self

class UserChoice(UserChoiceBody):
    def on_event(self, event):

        if event == 'device_locked' and self.choice == "1":
            return GetDataFromApi()
        if event == 'device_locked' and self.choice == "2":
            return self
        if event == 'device_locked' and self.choice == "3":
            return self
        if event == 'device_locked' and self.choice == "4":
            return self
        elif event == 'device_locked':
            return UserChoice()
        return self

class GetDataFromApi(GetDataFromApiBody):
    def on_event(self, event):

        if event == 'device_locked' and self.request_status == 200:
            return GetConnectionData(self.api_data)
        elif event == 'device_locked' and self.request_status != 200:
            return Error(self.error)
        return self

class GetConnectionData(GetConnectionDataBody):
    def on_event(self, event):

        if event == 'device_locked' and self.error == "":
            return InsertDbTablesBody(self.api_data, self.db)
        elif event == 'device_locked' and self.error != "":
            return Error(self.error)
        return self

class InsertDbTables(InsertDbTablesBody):
    def on_event(self, event):

        if event == 'device_locked':
            return UpdateDbTables(self.api_data, self.db)
        return self

class UpdateDbTables(UpdateDbTablesBody):
    def on_event(self, event):

        if event == 'device_locked':
            return UserChoice()
        return self

class Error(ErrorBody):
    def on_event(self, event):
        if event == 'device_locked' and self.choice.upper() == "Y":
            return Initialization()
        elif event != 'device_locked' or self.choice.upper() == "N":
            return self
        else:
            return Error(self.error)
