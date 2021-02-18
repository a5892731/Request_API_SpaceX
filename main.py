from system.menu import Menu, clear_screen
from system.user_selection import UserStateSelection
from system.system_states import booster_status_state, capsule_status_state, booster_serial_state, capsule_serial_state
from system.vehicles import Vehicles, Vehicle

if __name__ == "__main__":

    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}
    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}

    rockets = Vehicles("https://api.spacexdata.com/v4/cores").vehicles
    capsules = Vehicles("https://api.spacexdata.com/v4/capsules").vehicles



    state = 0

    while True:
        Menu(state)

        if state >= 111 and state < 118:
            booster_status_state(state, rockets, BOOSTERS_STATUS_DICT)

        elif state == 12:

            booster_serial_state(state, rockets, BOOSTERS_STATUS_DICT)

        elif state >= 211 and state < 217:
            capsule_status_state(state, capsules, CAPSULES_STATUS_DICT)

        elif state == 22:
            capsule_serial_state(state, capsules, CAPSULES_STATUS_DICT)

        elif state == 31:
            print(">>> >>> error: empty menu")

        elif state == 32:
            print(">>> >>> error: empty menu")


        user = UserStateSelection(state)
        state = user.return_state()

        clear_screen()