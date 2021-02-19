from system.vehicles import VehicleSort
from system.user_selection import UserSerialSelection
from system.lauches import LauchesSort

def booster_status_state(state, vehicles, STATUS_DICT):
    boosters = VehicleSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicles_by_status()

def booster_serial_state(state, vehicles, STATUS_DICT):
    user = UserSerialSelection()
    serial = user.return_serial()
    boosters = VehicleSort(state, vehicles, STATUS_DICT)
    boosters.print_vehicle_by_serial(serial)

def capsule_status_state(state, vehicles, STATUS_DICT):
    capsules = VehicleSort(state, vehicles, STATUS_DICT)
    capsules.print_vehicles_by_status()

def capsule_serial_state(state, vehicles, STATUS_DICT):
    user = UserSerialSelection()
    serial = user.return_serial()
    capsule = VehicleSort(state, vehicles, STATUS_DICT)
    capsule.print_vehicle_by_serial(serial)

def missions_future(lauches):
    missions = LauchesSort(lauches)
    missions.print_future_lauches()

def missions_previouse(lauches):
    missions = LauchesSort(lauches)
    missions.print_prefiouse_lauches()