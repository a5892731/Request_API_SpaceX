from system.vehicles import VehicleStatusSort



def booster_status_state(state, vehicles, STATUS_DICT):
    boosters = VehicleStatusSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicles()

def capsule_status_state(state, vehicles, STATUS_DICT):
    boosters = VehicleStatusSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicles()


