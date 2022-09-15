import os
import sys


class Settings():
    def __init__(self, path=os.path.abspath(sys.argv[0] + "/.." + "/..")):
        self.path = path + "/settings/settings.txt"
        self.settings = {}

    def change_setting(self, setting, newValue):
        self.settings[setting] = newValue
        self.write_settings()
        return 0

    def remember_key(self):
        return self.settings["random_key"]

    def write_settings(self):
        with open(self.path, "w") as file:
            for key, value in self.settings.items():
                toWrite = f"{key}:{value}\n"
                file.write(toWrite)

    def write_generated_key(self, databaseObject, username):
        generated_key = databaseObject.generateRandom(username)
        self.change_setting("random_key", generated_key)

    def delete_generated_key(self):
        self.change_setting("random_key", "0")

    def set_default_settings(self):
        current_path = os.path.abspath(sys.argv[0] + "/.." + "/..")
        settingDict = {"export_location": current_path + "/drawings",
                       "read_location": current_path + "/datas",
                       "export_extension": ".jpeg",
                       "color": "b",
                       "xlabel": "Axis x",
                       "ylabel": "Axis y",
                       "linestyle": "solid",
                       "dpi": "250",
                       "marker_plot": "None",
                       "marker_scatter": "o",
                       "random_key": None,
                       "legend_location": "upper left",
                       "mode": "pro",
                       "evervisited": "0"}
        self.settings = settingDict
        self.write_settings()
        return settingDict

    def read_settings(self):
        flag = 0
        with open(self.path, "a+") as file:
            file.seek(0)
            lines = file.readlines()
            settingsDict = dict()
            try:
                for line in lines:
                    if ":" not in line:
                        raise Exception("There is a problem in your settings!. All the settings are set to default.")
                    line = line.split(":")
                    settingsDict[line[0]] = line[1].strip()
            except:
                flag = 1
                print("There is a problem in your settings! All the settings are set to default!")
                self.set_default_settings()
                return 0
            if flag != 1:
                self.settings = settingsDict
                if self.settings["export_location"] == "None":
                    current_path = os.path.abspath(sys.argv[0] + "/../..") + "/drawings"
                    self.change_setting("export_location", current_path)
                if self.settings["read_location"] == "None":
                    current_path = os.path.abspath(sys.argv[0] + "/../..") + "/datas"
                    self.change_setting("read_location", current_path)
            if not settingsDict:
                print("There is a problem in your settings.")
                self.set_default_settings()

    def evervisited(self):
        if self.settings["evervisited"] == "0":
            return False
        else:
            return True

    def get_setting(self, settingName):
        try:
            return self.settings[settingName]
        except KeyError as KE:
            print(KE)
            print("--->>> There is a problem in your settings! All settings will set to default.")
            self.set_default_settings()
            return self.settings[settingName]

    def __str__(self):
        mystr = ""
        i = 0
        for key, value in self.settings.items():
            if key == "random_key" or key == "evervisited":
                continue
            tempo = f"{i}- {key:^25} -> {value:^25} \n"
            mystr += tempo
            i += 1
        return mystr[:-1]





