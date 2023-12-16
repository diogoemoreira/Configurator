class SingletonAlreadyExists(Exception):
    '''
    Exception raised when trying to create a singleton object which already exists
    '''

    def __init__(self):
        self.message = "The object you are trying to create is a singleton and is already instantiated."
    
    def __str__(self):
        return self.message
    
class SingletonNotInstantiated(Exception):
    '''
    Exception raised when trying to access an instance of a singleton which has yet to be created
    '''

    def __init__(self):
        self.message = "The instance you are trying to access was never instantiated."
    
    def __str__(self):
        return self.message

class ConfigurationAlreadyExists(Exception):
    '''
    Exception raised when trying to create a new configuration using an existing configuration's name
    '''

    def __init__(self):
        self.message = "The name you are trying to use already exists. Please choose a new name for the new configuration or update the already existing one."

    def __str__(self):
        return self.message
    
class InvalidConfigurationParameters(Exception):
    '''
    Exception raised when a new configuration's parameters don't follow the stipulated format
    '''

    def __init__(self):
        self.message = "The format you are trying to use is invalid. Please use the following format:\nFor a single parameter:\nkey:value\n\nFor multiple parameters:\nkey:value,key:value"

    def __str__(self):
        return self.message
    
class UpdateInvalidConfiguration(Exception):
    '''
    Exception raised when trying to update the configuration using a nonexistent configuration's name
    '''

    def __init__(self):
        self.message = "The configuration you are trying to update does not exist. Please use an existing configuration's name."

    def __str__(self):
        return self.message

class LoadInvalidFile(Exception):
    '''
    Exception raised when trying to load an invalid file
    '''

    def __init__(self):
        self.message = "The file you are trying to load does not exist or has an invalid format."

    def __str__(self):
        return self.message
