import requests
import json
import pprint

class Capsule:
    def __init__(self, type, reuse_count, last_update, launches, serial, id, status, *args, **kwargs):
        self.type = type
        self.reuse_count = reuse_count
        self.last_update = last_update
        self.launches = launches
        self.serial = serial
        self.id = id
        self.status = status

    def printing_capsule_all_data(self):
        print("type: {}".format(self.type))
        print("reuse_count: {}".format(self.reuse_count))
        print("last_update: {}".format(self.last_update))
        print("launches: {}".format(self.launches))
        print("serial: {}".format(self.serial))
        print("id: {}".format(self.id))
        print("status: {}".format(self.status))

    def printing_capsule_data(self):
        print("serial: {}".format(self.serial))
        print("reuse_count: {}".format(self.reuse_count))
        print("status: {}".format(self.status))

class Capsules:
    capsules = []
    def __init__(self, capsule: Capsule):

        r = requests.get("https://api.spacexdata.com/v4/capsules")
        try:
            spacex_data = r.json()
        except json.decoder.JSONDecodeError:
            print("wrong format")
        else:
            for element in spacex_data:
                self.capsules.append(capsule(element["type"], element["reuse_count"], element["last_update"],
                                           element["launches"], element["serial"], element["id"], element["status"]))


if __name__ == "__main__":
    spacex = Capsules(Capsule)
    spacex.capsules[2].printing_rocket_data()
