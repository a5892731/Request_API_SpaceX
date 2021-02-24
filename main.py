'''
version 1.2
author: a5892731
date: 2021-02-24
'''

#from system.menu import Menu, clear_screen
from system_v2.menu import Menu, clear_screen
from system.user_selection import UserStateSelection
from system.system_states import booster_status_state, capsule_status_state, booster_serial_state, \
    capsule_serial_state, missions_previouse, missions_future
from system.vehicles import Vehicles
from system.lauches import Launches

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

    API_ADDRESS_DICT = {
                        "BOOSTERS": "https://api.spacexdata.com/v4/cores",
                        "CAPSULES": "https://api.spacexdata.com/v4/capsules",
                        "MISSIONS": "https://api.spacexdata.com/v4/launches"
                        }

    rockets = []
    capsules = []
    lauches = []
    state = 0

    while True:
        #Menu(state, BOOSTERS_MENU_DICT, BOOSTERS_STATUS_DICT, CAPSULES_STATUS_DICT, CAPSULES_MENU_DICT, MISSIONS_DICT)
        menu = Menu(state, MENU_DICT)
        menu.drow_menu()

        if state >= 111 and state < 118:

            if rockets == []:
                    rockets = Vehicles(API_ADDRESS_DICT["BOOSTERS"]).vehicles
                    print(">Data received")
            booster_status_state(state, rockets, BOOSTERS_STATUS_DICT)

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
            if lauches == []:
                    lauches = Lauches(API_ADDRESS_DICT["MISSIONS"]).lauches
                    print(">Data received")
            missions_previouse(lauches)

        elif state == 32:
            if lauches == []:
                    lauches = Lauches(API_ADDRESS_DICT["MISSIONS"]).lauches
                    print(">Data received")
            missions_future(lauches)

        user = UserStateSelection(state)
        state = user.return_state()
        clear_screen()
