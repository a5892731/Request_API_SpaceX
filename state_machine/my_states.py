'''
here are the rules of state transition
'''

from state_machine.states.initialization import InitializationBody
from state_machine.states.get_connection_data import GetConnectionDataBody
from state_machine.states.get_data_frim_api_for_table import GetDataFrimApiForTableBody
from state_machine.states.create_menu_list import CreateMenuListBody
from state_machine.states.print_menu import PrintMenuBody
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
            return GetDataFrimApiForTable()
        return self

class GetDataFrimApiForTable(GetDataFrimApiForTableBody):
    def on_event(self, event):
        if event == 'device_locked':
            return CreateMenuList()
        return self

class CreateMenuList(CreateMenuListBody):
    def on_event(self, event):
        if event == 'device_locked':
            return PrintMenu()
        return self

class PrintMenu(PrintMenuBody):
    def on_event(self, event):
        if event == 'device_locked':
            return UserChoice()
        return self

class UserChoice(UserChoiceBody):
    def on_event(self, event):
        if event == 'device_locked':
            return Initialization()
        return self