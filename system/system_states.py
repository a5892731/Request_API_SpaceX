from system.rockets import Rockets, Rocket
from system.capsules import Capsules, Capsule

class BoostersStatus:

    BOOSTERS_STATUS_DICT = {111: "active", 112: "inactive", 113: "unknown",
                            114: "inactive", 115: "expended", 116: "lost"}

    def __init__(self, state, rockets: Rockets):
        self.rockets = rockets
        self.state = state

    def print_rockets(self):
        number_of_rockets = 1

        for rocket in self.rockets:
            if rocket.status == self.BOOSTERS_STATUS_DICT[self.state]:
                print("\n{}: ".format(number_of_rockets))
                rocket.printing_rocket_data()
                number_of_rockets += 1

class CapsuleStatus:

    CAPSULES_STATUS_DICT = {211: "active", 212: "inactive", 213: "unknown",
                            214: "inactive", 215: "expended", 216: "lost"}

    def __init__(self, state, capsules: Capsules):
        self.capsules = capsules
        self.state = state

    def print_capsules(self):
        number_of_capsules = 1

        for rocket in self.capsules:
            if rocket.status == self.CAPSULES_STATUS_DICT[self.state]:
                print("\n{}: ".format(number_of_capsules))
                rocket.printing_capsule_data()
                number_of_capsules += 1


