'''
version 1.2
author: a5892731
date: 2021-02-24
'''


#from system.menu import Menu, clear_screen

from system.user_selection import UserStateSelection
from system.system_states import booster_status_state, capsule_status_state, booster_serial_state, \
    capsule_serial_state, missions_previouse, missions_future
from system.vehicles import Vehicles
from system.lauches import Launches

from system_v2.menu import Menu, SmartMenu, clear_screen
from system_v2.spacex_data_container import SpacexObjects, ObjectsSort

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

    API_ADDRESS_DICT = {
                        "BOOSTERS": "https://api.spacexdata.com/v4/cores",
                        "CAPSULES": "https://api.spacexdata.com/v4/capsules",
                        "MISSIONS": "https://api.spacexdata.com/v4/launches"
                        }

    rockets = []
    capsules = []
    launches = []
    state = 0

#---------------------------------------------------------------------------------------
    def request_data(data_list, API_ADDRESS, OBJECTS_DICT):

        if data_list == []:
            data_list = SpacexObjects(API_ADDRESS, OBJECTS_DICT).objects
            print(">Data received")
        return data_list

#--------------------------------------------------------------------------------------- <<<< MAIN MENU

    menu = SmartMenu(MENU_DICT)

    while True:
        #Menu(state, BOOSTERS_MENU_DICT, BOOSTERS_STATUS_DICT, CAPSULES_STATUS_DICT, CAPSULES_MENU_DICT, MISSIONS_DICT)
        menu.cover_menu_by_state(state)
        menu.drow_menu()

        if state >= 111 and state < 118:

            rockets = request_data(rockets, API_ADDRESS_DICT["BOOSTERS"], BOOSTERS_OBJECT_DICTIONARY)

            sorted_rockets = ObjectsSort(rockets)
            sorted_rockets.print_objects_by_status("active", {
                "block": "", "reuse_count": "",
                "serial": "", })

            #if rockets == []:
            #     rockets = Vehicles(API_ADDRESS_DICT["BOOSTERS"]).vehicles
            #      print(">Data received")

            #booster_status_state(state, rockets, BOOSTERS_STATUS_DICT)

        elif state == 12:
            if rockets == []:
                    rockets = Vehicles(API_ADDRESS_DICT["BOOSTERS"]).vehicles
                    print(">Data received")
            booster_serial_state(state, rockets, BOOSTERS_STATUS_DICT)

        elif state >= 211 and state < 217:
            if capsules == []:
                    capsules = Vehicles(API_ADDRESS_DICT["CAPSULES"]).vehicles
            capsule_status_state(state, capsules, CAPSULES_STATUS_DICT)

        elif state == 22:
            if capsules == []:
                    capsules = Vehicles(API_ADDRESS_DICT["CAPSULES"]).vehicles
                    print(">Data received")
            capsule_serial_state(state, capsules, CAPSULES_STATUS_DICT)

        elif state == 31:
            if launches == []:
                    launches = Launches(API_ADDRESS_DICT["MISSIONS"]).launches
                    print(">Data received")
            missions_previouse(launches)

        elif state == 32:
            if launches == []:
                    launches = Launches(API_ADDRESS_DICT["MISSIONS"]).launches
                    print(">Data received")
            missions_future(launches)

        user = UserStateSelection(state)
        state = user.return_state()
        clear_screen()
