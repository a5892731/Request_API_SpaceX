
import requests
import json
import pprint


class Rocket:
    def __init__(self, block, reuse_count, last_update, launches, serial, id, status, *args, **kwargs):
        self.block = block
        self.reuse_count = reuse_count
        self.last_update = last_update
        self.launches = launches
        self.serial = serial
        self.id = id
        self.status = status

    def printing_rocket_all_data(self):
        print("block: {}".format(self.block))
        print("reuse_count: {}".format(self.reuse_count))
        print("last_update: {}".format(self.last_update))
        print("launches: {}".format(self.launches))
        print("serial: {}".format(self.serial))
        print("id: {}".format(self.id))
        print("status: {}".format(self.status))

    def printing_rocket_data(self):
        print("serial: {}".format(self.serial))
        print("reuse_count: {}".format(self.reuse_count))
        print("status: {}".format(self.status))



class Rockets:
    rockets = []
    def __init__(self, rocket: Rocket):

        r = requests.get("https://api.spacexdata.com/v4/cores")
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.rockets.append(rocket(element["block"], element["reuse_count"], element["last_update"],
                                           element["launches"], element["serial"], element["id"], element["status"]))


if __name__ == "__main__":
    spacex = Rockets(Rocket)
    spacex.rockets[50].printing_rocket_data()
