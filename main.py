from system.menu import Menu, clear_screen
from system.user_selection import UserSelection
from system.system_states import BoostersStatus, CapsuleStatus
from system.rockets import Rockets, Rocket
from system.capsules import Capsules, Capsule


if __name__ == "__main__":

    state = 0
    rockets = Rockets(Rocket).rockets
    capsules = Capsules(Capsule).capsules

    while True:

        Menu(state)
        user = UserSelection(state)
        state = user.return_state()


        if state >= 111 and state < 117:
            boosters = BoostersStatus(state, rockets)
            boosters.print_rockets()

        if state >= 211 and state < 217:
            boosters = CapsuleStatus(state, capsules)
            boosters.print_capsules()





        state = user.return_state()
        clear_screen()