from system.menu import Menu, clear_screen
from system.user_selection import UserSelection
from system.system_states import booster_status_state, capsule_status_state
from system.vehicles import Vehicles, Vehicle

if __name__ == "__main__":

    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}

    state = 0


    rockets = Vehicles(Vehicle, "https://api.spacexdata.com/v4/cores").vehicles
    capsules = Vehicles(Vehicle, "https://api.spacexdata.com/v4/capsules").vehicles

    while True:

        Menu(state)
        user = UserSelection(state)
        state = user.return_state()


        if state >= 111 and state < 117:
            booster_status_state(state, rockets, BOOSTERS_STATUS_DICT)

        if state >= 211 and state < 217:
            capsule_status_state(state, capsules, CAPSULES_STATUS_DICT)





        state = user.return_state()
        clear_screen()