'''
version 1.6
author: a5892731
date: 2021-03-01

required modules:

>>> terminaltables
>>> requests
>>> json

>>> os , platform, datetime
'''



from system_v2.user_selection import UserStateSelection
from system_v2.system_states import SystemStates
from system_v2.menu import SmartMenu, clear_screen
from system_v2.read_data_files import DataImport

#---------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------- <<<< MAIN MENU

if __name__ == "__main__":

    HEADING_MENU_DICT = {1: "BOOSTERS", 2: "CAPSULES", 3: "LAUNCHES"}
    BOOSTERS_MENU_DICT = {11 : "STATUS", 12: "SERIAL"}
    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_MENU_DICT = {21 : "STATUS", 22: "SERIAL"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}
    MISSIONS_DICT = {31 : "PREVIOUS", 32 : "FUTURE", 33: "OBJECT NUMBER", 34: "SORT OBJECTS\n    BY TIME"}

    MENU_DICT = [
                HEADING_MENU_DICT,
                [BOOSTERS_MENU_DICT, CAPSULES_MENU_DICT, MISSIONS_DICT],
                [BOOSTERS_STATUS_DICT,CAPSULES_STATUS_DICT, {}]
                ]



    BOOSTERS_OBJECT_CALL_LIST = DataImport("BOOSTERS_OBJECT_LIST.txt", "list")
    SHORT_BOOSTERS_OBJECT_CALL_LIST = DataImport("SHORT_BOOSTERS_OBJECT_LIST.txt", "list")
    VERY_SHORT_BOOSTERS_OBJECT_CALL_LIST = DataImport("VERY_SHORT_BOOSTERS_OBJECT_LIST.txt", "list")

    CAPSULES_OBJECT_CALL_LIST = DataImport("CAPSULES_OBJECT_LIST.txt", "list")
    SHORT_CAPSULES_OBJECT_CALL_LIST = DataImport("SHORT_CAPSULES_OBJECT_LIST.txt", "list")
    VERY_SHORT_CAPSULES_OBJECT_CALL_LIST = DataImport("VERY_SHORT_CAPSULES_OBJECT_LIST.txt", "list")

    LAUNCHES_OBJECT_CALL_LIST = DataImport("LAUNCHES_OBJECT_LIST.txt", "list")
    SHORT_LAUNCHES_OBJECT_CALL_LIST = DataImport("SHORT_LAUNCHES_OBJECT_LIST.txt", "list")
    VERY_SHORT_LAUNCHES_OBJECT_CALL_LIST = DataImport("VERY_SHORT_LAUNCHES_OBJECT_LIST.txt", "list")


    API_ADDRESS_CALL_DICT = DataImport("API_ADDRESS_DICT.txt", "dict")


    boosters = []
    capsules = []
    launches = []
    state = 0


    system_states = SystemStates()

    menu = SmartMenu(MENU_DICT)


    while True:
        menu.cover_menu_by_state(state)
        menu.drow_menu()

        if state >= 111 and state < 118:
            system_states.booster_status_state(BOOSTERS_OBJECT_CALL_LIST(), VERY_SHORT_BOOSTERS_OBJECT_CALL_LIST(),
                                               API_ADDRESS_CALL_DICT()["BOOSTERS"], BOOSTERS_STATUS_DICT[state],
                                               "status")
        elif state == 12:
            system_states.booster_serial_state(BOOSTERS_OBJECT_CALL_LIST(), SHORT_BOOSTERS_OBJECT_CALL_LIST(),
                                               API_ADDRESS_CALL_DICT()["BOOSTERS"],
                                               input(">>> Put booster serial number: "), "serial")
        elif state >= 211 and state < 217:
            system_states.capsule_status_state(CAPSULES_OBJECT_CALL_LIST(), VERY_SHORT_CAPSULES_OBJECT_CALL_LIST(),
                                               API_ADDRESS_CALL_DICT()["CAPSULES"], CAPSULES_STATUS_DICT[state],
                                               "status")
        elif state == 22:
            system_states.capsule_serial_state(CAPSULES_OBJECT_CALL_LIST(), SHORT_CAPSULES_OBJECT_CALL_LIST(),
                                               API_ADDRESS_CALL_DICT()["CAPSULES"],
                                               input(">>> Put capsule serial number: "), "serial")
        elif state == 31:
            system_states.missions_previouse(LAUNCHES_OBJECT_CALL_LIST(), VERY_SHORT_LAUNCHES_OBJECT_CALL_LIST(),
                                             API_ADDRESS_CALL_DICT()["LAUNCHES"])

        elif state == 32:
            system_states.missions_future(LAUNCHES_OBJECT_CALL_LIST(), SHORT_LAUNCHES_OBJECT_CALL_LIST(),
                                          API_ADDRESS_CALL_DICT()["LAUNCHES"])

        elif state == 33:
            system_states.missions_object_number_state(LAUNCHES_OBJECT_CALL_LIST(), LAUNCHES_OBJECT_CALL_LIST(),
                                                       API_ADDRESS_CALL_DICT()["LAUNCHES"],
                                                       input(">>> Put launch object number: "), "OBJECT NUMBER")

        elif state == 34:
            system_states.missions_sort_by_time(LAUNCHES_OBJECT_CALL_LIST(), [], API_ADDRESS_CALL_DICT()["LAUNCHES"])
            #print(">>> 404 - FUNCTION IN PROGRESS")


        user = UserStateSelection(state)
        state = user.return_state()
        clear_screen()
