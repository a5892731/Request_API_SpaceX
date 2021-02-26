'''
version 1.5
author: a5892731
date: 2021-02-26
'''



from system_v2.user_selection import UserStateSelection
from system_v2.system_states import booster_status_state, booster_serial_state, capsule_status_state, \
                                    capsule_serial_state, missions_future, missions_previouse
from system_v2.menu import Menu, SmartMenu, clear_screen
from system_v2.read_data_files import DataImport

if __name__ == "__main__":

    HEADING_MENU_DICT = {1: "BOOSTERS", 2: "CAPSULES", 3: "MISSIONS"}
    BOOSTERS_MENU_DICT = {11 : "STATUS", 12: "SERIAL"}
    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_MENU_DICT = {21 : "STATUS", 22: "SERIAL"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}
    MISSIONS_DICT = {31 : "PREVIOUS", 32 : "FUTURE"}

    MENU_DICT = [
                HEADING_MENU_DICT,
                [BOOSTERS_MENU_DICT, CAPSULES_MENU_DICT, MISSIONS_DICT],
                [BOOSTERS_STATUS_DICT,CAPSULES_STATUS_DICT, {}]
                ]

    BOOSTERS_OBJECT_DICTIONARY = {
                            "block": "", "reuse_count": "", "last_update": "", "launches": "",
                             "serial": "", "id": "", "status": "",
                         }

    CAPSULES_OBJECT_DICTIONARY = {
                            "type": "", "reuse_count": "", "last_update": "", "launches": "",
                             "serial": "", "id": "", "status": "",
                         }

    LAUNCHES_OBJECT_DICTIONARY = {
                            "fairings": "", "links": "", "static_fire_date_utc": "", "rocket": "",
                             "success": "", "details": "", "crew": "", "capsules": "", "payloads": "",
                             "failures": "", "flight_number": "", "name": "", "date_utc": "", "cores": "",
                             "id": "",
                                }


    API_ADDRESS_CALL_DICT = DataImport("API_ADDRESS_DICT.txt", "dict")


    boosters = []
    capsules = []
    launches = []
    state = 0

#---------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------- <<<< MAIN MENU

if __name__ == "__main__":

    menu = SmartMenu(MENU_DICT)

    while True:
        menu.cover_menu_by_state(state)
        menu.drow_menu()

        if state >= 111 and state < 118:

            boosters = booster_status_state(state, boosters, BOOSTERS_OBJECT_DICTIONARY, BOOSTERS_STATUS_DICT,
                                            API_ADDRESS_CALL_DICT()["BOOSTERS"])

        elif state == 12:

            boosters = booster_serial_state(state, boosters, BOOSTERS_OBJECT_DICTIONARY,
                                            API_ADDRESS_CALL_DICT()["BOOSTERS"])

        elif state >= 211 and state < 217:

            capsules = capsule_status_state(state, capsules, CAPSULES_OBJECT_DICTIONARY, CAPSULES_STATUS_DICT,
                                            API_ADDRESS_CALL_DICT()["CAPSULES"])

        elif state == 22:

            capsules = capsule_serial_state(state, capsules, CAPSULES_OBJECT_DICTIONARY,
                                            API_ADDRESS_CALL_DICT()["CAPSULES"])

        elif state == 31:

            launches = missions_previouse(LAUNCHES_OBJECT_DICTIONARY, API_ADDRESS_CALL_DICT()["MISSIONS"], launches)

        elif state == 32:

            launches = missions_future(LAUNCHES_OBJECT_DICTIONARY, API_ADDRESS_CALL_DICT()["MISSIONS"], launches)


        user = UserStateSelection(state)
        state = user.return_state()
        clear_screen()
