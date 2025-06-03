import json

class BlackOsCore:
    def __init__(self):
        self.load_config()

    def load_config(self):
        with open("system/config.json", "r") as file:
            self.config = json.load(file)

    def get_version(self):
        return self.config["version"]

    def start_system(self):
        print("BlackOs Kernel Loaded.")