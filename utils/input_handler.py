import re
from utils.error_handling import *
from utils.file_handler import *

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
            Menu.__multiple_pattern = re.compile(r'\s*([^:]+)\s*:\s*"([^"]*)"\s*(?:\s*([^:]+)\s*:\s*"([^"]*)")?')
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

            option = Menu.__input_choice()
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
                Menu.__update_config()
            elif option == "save":
                Menu.__save_json_file()
            elif option == "load":
                Menu.__load_json_file()
            elif option == "exit":
                if Menu.__confirm_choice("exit"):
                    print("\nExiting configurator...")
                    exit()
            else:
                print("\n"+str(OptionDoesNotExist()))



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
        return input("Choose an option: ")


    ## menu functionalities
    def __reset_config():
        #resets the current configurations
        Menu.configurations = dict()

    def __add_config():
        #add a new configuration to the configurations dictionary
        print("Add a new configuration.\n")
        new_config_name = input("What would you like to name the new configuration as: ")
        
        #check if the given name already exists in the current configurations
        if new_config_name in Menu.configurations:
            print("\n"+str(ConfigurationAlreadyExists()))
            return
        
        new_configs_params = input("\nPlease enter the configuration's parameters using the specified format. You can enter multiple values.  \
                            \n key: \"value\"\n\nConfiguration parameters:\n")

        Menu.__new_config_value(new_config_name, new_configs_params)

    def __display_config():
        #display the current configurations
        print("\nCurrent Configurations:")

        for key, value in Menu.configurations.items():
            print(f"{key}: {value}")

    def __update_config():
        #update the parameters of an already existing configuration
        config_name = input("What's the name of the configuration you wish to update?")

        if config_name not in Menu.configurations:
            print("\n"+ str(UpdateInvalidConfiguration()))
            return
        
        new_configs_params = input("\nPlease enter the new configuration's parameters using the specified format. You can enter multiple values. \
                            \n key: \"value\"\n\nConfiguration parameters:\n")

        Menu.__new_config_value(config_name, new_configs_params)


    def __new_config_value(config_name, new_configs_params):
        #Validate input format for single and multiple parameters
        matches = Menu.__single_pattern.match(new_configs_params)
        #match_groups = matches.groups()
        if not matches:
            match_groups = Menu.__multiple_pattern.findall(new_configs_params)
            if not match_groups:
                print("\n"+str(InvalidConfigurationParameters()))
                return
            match_groups = [item for sublist in match_groups for item in sublist if item!='']

        match_dict= dict()
        for i in range(0,len(match_groups)-1,2):
            match_dict[match_groups[i]] = match_groups[i+1]
        
        #Create a dictionary to hold the new parameters for the configuration
        Menu.configurations[config_name] = dict()
        #Add the parameters to the new dictionary
        for key, value in match_dict.items():
            Menu.configurations[config_name][key] = value


    def __save_json_file():
        file_name = input("Which name do you wish to use for the file? (it should end with .json)\n")
        FileHandler.save_to_file(file=file_name, configurations=Menu.configurations)

    def __load_json_file():
        file_name = input("What is the name of the file you wish to load? (it should end with .json)\n")
        new_configs = FileHandler.read_file(file_name)

        if new_configs!=None:
            Menu.configurations=new_configs

    def __confirm_choice(choice):
        #choice - the option which should be confirmed
        print("Are you sure you wish to "+ choice+"? (yes/no)")
        
        user_choice = input()
        if(user_choice.strip()=="yes"):
            return True
        elif(user_choice.strip()=="no"):
            return False
