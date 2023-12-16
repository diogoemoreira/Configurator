import json
from utils.error_handling import *

class FileHandler():

    __instance = None

    def __init__(self):
        if FileHandler.__instance!=None:
            raise SingletonAlreadyExists()
        else:
            FileHandler.__instance=self

    @staticmethod
    def get_instance():
        if FileHandler.__instance==None:
            raise SingletonNotInstantiated()
        else:
            return FileHandler.__instance

    def save_to_file(file, configurations):
        try:
            json_object = json.dumps(configurations, indent=4)
        except:
            print("\n"+str(SaveInvalidFile()))
            return False

        with open(str(file), "w") as outfile:
            outfile.write(json_object)
    
    def read_file(file):
        configurations = dict()

        with open(str(file), "r") as openfile:
            try:
                configurations = json.loads(s=openfile.read())
            except:
                print("\n"+str(LoadInvalidFile()))
                return None

        return configurations