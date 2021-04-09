'''
here are the rules of state transition
'''

from state_machine.states.initialization.initialization import InitializationBody
from state_machine.states.update.get_connection_data import GetConnectionDataBody
from state_machine.states.update.get_api import GetDataFromApiBody
from state_machine.states.initialization.user_choice import UserChoiceBody
from state_machine.states.error.error import ErrorBody
from state_machine.states.update.insert_db_tables import InsertDbTablesBody
from state_machine.states.update.update_db_tables import UpdateDbTablesBody
from state_machine.states.settings.settings import SetingsBody
from state_machine.states.read_db.read_database import ReadDbBody
from state_machine.states.update.read_db_tables_len import ReadDbTablesLenBody
from state_machine.states.close.close import CloseBody
from state_machine.states.read_db.launches.read_launches import LaunchesBody
from state_machine.states.read_db.boosters.read_boosters import BoostersBody
from state_machine.states.read_db.capsules.read_capsules import CapsulesBody
from state_machine.states.read_db.rockets.read_rockets import RocketsBody
from state_machine.states.read_db.crew.read_crew import CrewBody
from state_machine.states.read_db.payloads.read_payloads import PayloadsBody
from state_machine.states.read_db.ships.read_ships import ShipsBody
from state_machine.states.read_db.launchpads.read_launchpads import LaunchpadsBody
from state_machine.states.read_db.landpads.read_landpads import LandpadsBody
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
            elif event == 'device_locked' and self.choice == "4":
                return Rockets()
            elif event == 'device_locked' and self.choice == "5":
                return Crew()
            elif event == 'device_locked' and self.choice == "6":
                return Payloads()
            elif event == 'device_locked' and self.choice == "7":
                return Ships()
            elif event == 'device_locked' and self.choice == "8":
                return Launchpads()
            elif event == 'device_locked' and self.choice == "9":
                return Landpads()
            elif event == 'device_locked':
                return UserChoice()
            return self
        except AttributeError:
            return Error("Database <spacex> does not exist. Update database before reading!")

class Launches(LaunchesBody):
    def on_event(self, event):
        if event == 'device_locked' and self.go_back == True:
            return ReadDb()
        elif event == 'device_locked' and self.go_back == False:
            return Launches()
        return self

class Boosters(BoostersBody):
    def on_event(self, event):
        if event == 'device_locked' and self.go_back == True:
            return ReadDb()
        elif event == 'device_locked' and self.go_back == False:
            return Boosters()
        return self

class Capsules(CapsulesBody):
    def on_event(self, event):
        if event == 'device_locked' and self.go_back == True:
            return ReadDb()
        elif event == 'device_locked' and self.go_back == False:
            return Capsules()
        return self

class Rockets(RocketsBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
        return self

class Payloads(PayloadsBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
        return self

class Crew(CrewBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
        return self

class Ships(ShipsBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
        return self

class Launchpads(LaunchpadsBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
        return self

class Landpads(LandpadsBody):
    def on_event(self, event):
        if event == 'device_locked':
            return ReadDb()
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
