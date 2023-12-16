from utils.error_handling import *

class Menu():
    '''
    Menu class uses the Singleton pattern as there should only be 
    one menu running at a time
    '''
    __instance = None

    def __init__(self) -> None:
        if Menu.__instance!=None:
            raise SingletonAlreadyExists()
        else:
            __instance=self
    
    @staticmethod
    def get_instance():
        if Menu.__instance==None:
            raise SingletonNotInstantiated()
        else:
            return Menu.__instance
        
    def menu():
        print("Welcome to the configurator application.\
              \nThis application serves to help you generate your configurations \
              allowing you to save and load them from a JSON file.\
              \n\nWhenever you wish to start a new empty configuration you can use the 'reset' option.")

        while(True):
            option=None
            Menu.__menu_options()

            option = input("Choose an option: ")
            while(option==None):
                print("-- Please choose a valid option --\n\n")
                Menu.__menu_options()
                option = input("Choose an option: ")
            
            option = option.strip().lower()
            if option == "reset":
                print("reset")
                pass
            elif option == "add":
                print("add")
                pass
            elif option == "display":
                print("display")
                pass
            elif option == "update":
                print("update")
                pass
            elif option == "save":
                print("save")
                pass
            elif option == "load":
                print("load")
                pass
            elif option == "exit":
                print("\nExiting configurator...")
                exit()
            else:
                print("\nPlease choose a valid option.\n")

    def __menu_options():
        print("{:<10} - {}".format("[reset]", "Reset configurations"))
        print("{:<10} - {}".format("[add]", "Add new configuration"))
        print("{:<10} - {}".format("[display]", "Display current configurations"))
        print("{:<10} - {}".format("[save]", "Save configurations to a file"))
        print("{:<10} - {}".format("[load]", "Load configurations from a file"))
        print("{:<10} - {}".format("[exit]", "Exit\n"))