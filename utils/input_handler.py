import re
from utils.error_handling import *

class Menu():
    '''
    Menu class uses the Singleton pattern as there should only be 
    one menu running at a time
    '''

    configurations = dict()
    __instance = None
    __single_pattern = None
    __multiple_pattern = None

    def __init__(self):
        if Menu.__instance!=None:
            raise SingletonAlreadyExists()
        else:
            #this pattern captures key, value pairs in the stipulated format
            #key: "value", key: "value"
            #being able to repeat key: "value" as many times as needed
            Menu.__single_pattern = re.compile(r'\s*([^:]+)\s*:\s*"([^"]*)"\s*$')
            Menu.__multiple_pattern = re.compile(r'\s*([^:]+)\s*:\s*"([^"]*)"\s*(?:,\s*([^:]+)\s*:\s*"([^"]*)")?\s*$')
            Menu.__instance=self
    
    @staticmethod
    def get_instance():
        if Menu.__instance==None:
            raise SingletonNotInstantiated()
        else:
            return Menu.__instance
        
    def menu(self):
        print("Welcome to the configurator application.\
              \nThis application serves to help you generate your configurations allowing you to save and load them from a JSON file.\
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
                Menu.__reset_config()
            elif option == "add":
                Menu.__add_config()
            elif option == "display":
                Menu.__display_config()
            elif option == "update":
                print("update")
            elif option == "save":
                print("save")
            elif option == "load":
                print("load")
            elif option == "exit":
                if Menu.__confirm_choice("exit"):
                    print("\nExiting configurator...")
                    exit()
            else:
                print("\nPlease choose a valid option.\n")

    def __menu_options():
        print()
        print("{:<10} - {}".format("[reset]", "Reset configurations."))
        print("{:<10} - {}".format("[add]", "Add new configuration."))
        print("{:<10} - {}".format("[display]", "Display current configurations."))
        print("{:<10} - {}".format("[update]", "Update a configuration using its name."))
        print("{:<10} - {}".format("[save]", "Save configurations to a file."))
        print("{:<10} - {}".format("[load]", "Load configurations from a file."))
        print("{:<10} - {}".format("[exit]", "Exit.\n"))

    def __input_choice():
        pass

    def __reset_config():
        Menu.configurations = dict()

    def __add_config():
        print("Add a new configuration.\n")
        new_config_name = input("What would you like its name to be: ")
        
        if new_config_name in Menu.configurations:
            print("\n"+str(ConfigurationAlreadyExists()))
            return
        
        new_configs_params = input("\nPlease enter the configuration's parameters using the specicified format. \
                            \n key: \"value\"\
                            \nFor multiple values separate them using a semi-colon \";\"\
                            Example:\n param1: \"value for param1\"; param2: \"valueforparam2!\"\nConfiguration parameters:\n")

        matches = Menu.__single_pattern.match(new_configs_params)
    
        if not matches:
            # Validate input format
            matches = re.fullmatch(Menu.__multiple_pattern, new_configs_params)
            if not matches:
                print("\n"+str(InvalidConfigurationParameters()))
                return

        match_groups = matches.groups()

        match_dict= dict()
        for i in range(len(match_groups)-1):
            match_dict[match_groups[i]] = match_groups[i+1]
            i+=1
        
        #Create a dictionary to hold the new parameters for the configuration
        Menu.configurations[new_config_name] = dict()
        #Add the parameters to the new dictionary
        for key, value in match_dict.items():
            Menu.configurations[new_config_name][key] = value

    def __display_config():
        print("\nCurrent Configurations:\n")

        for key, value in Menu.configurations.items():
            print(f"{key}: {value}")

    def __confirm_choice(choice):
        #choice - the option which should be confirmed
        print("Are you sure you wish to "+ choice+"? (yes/no)")
        
        user_choice = input()
        if(user_choice.strip()=="yes"):
            return True
        elif(user_choice.strip()=="no"):
            return False
