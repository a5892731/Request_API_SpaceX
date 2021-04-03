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
from state_machine.states.settings import SetingsBody
from state_machine.states.read_database import ReadDbBody
from state_machine.states.read_db_tables_len import ReadDbTablesLenBody
from state_machine.states.close import CloseBody
from state_machine.states.read_launches import LaunchesBody
from state_machine.states.read_boosters import BoostersBody
from state_machine.states.read_capsules import CapsulesBody
# Start of our states <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



class Initialization(InitializationBody):
    def on_event(self, event):

        if event == 'device_locked':
            return UserChoice()
        return self

class UserChoice(UserChoiceBody):
    def on_event(self, event):

        #return_dict = {"1": GetDataFromApi(), "2": ReadDb(), "3": Setings(), "4": UserChoice()}


        if event == 'device_locked' and self.choice == "1":
            return GetDataFromApi()
        elif event == 'device_locked' and self.choice == "2":
            return ReadDb()
        elif event == 'device_locked' and self.choice == "3":
            return Setings()
        elif event == 'device_locked' and self.choice == "4":
            return self
        elif event == 'device_locked':
            return UserChoice()

        else:
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
            return ReadDbTablesLen(self.api_data, self.db)
        elif event == 'device_locked' and self.error != "":
            return Error(self.error)
        else:
            return self
        return self

class ReadDbTablesLen(ReadDbTablesLenBody):
    def on_event(self, event):

        if event == 'device_locked':
            return InsertDbTables(self.api_data, self.db, self.db_sizes)
        elif event == 'device_locked' and self.error != "":
            return Error(self.error)
        else:
            return self
        return self

class InsertDbTables(InsertDbTablesBody):
    def on_event(self, event):

        if event == 'device_locked':
            return UpdateDbTables(self.api_data, self.db)
        return self

class UpdateDbTables(UpdateDbTablesBody):  # not in use <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def on_event(self, event):
        if event == 'device_locked':
            return UserChoice()
        return self
#-------------------------------------------------------------------------------------------------------------
class ReadDb(ReadDbBody):
    def on_event(self, event):

        try:
            if event == 'device_locked' and self.choice == "1":
                return Launches()
            elif event == 'device_locked' and self.choice == "2":
                return Boosters()
            elif event == 'device_locked' and self.choice == "3":
                return Capsules()
            elif event == 'device_locked':
                return UserChoice()
            return self
        except AttributeError:
            return Error("Database <spacex> does not exist. Update database before reading!")


class Launches(LaunchesBody):
    def on_event(self, event):
        if event == 'device_locked':
            return UserChoice()
        return self

class Boosters(BoostersBody):
    def on_event(self, event):
        if event == 'device_locked':
            return UserChoice()
        return self

class Capsules(CapsulesBody):
    def on_event(self, event):
        if event == 'device_locked':
            return UserChoice()
        return self

#-------------------------------------------------------------------------------------------------------------
class Setings(SetingsBody): # not in use <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

class Close(CloseBody):
    def on_event(self, event):
        return self
