# Configurator
A Python script that acts as a quick configurator for a system component. The script allows users to generate configurations, navigate menus efficiently, and persist configurations in JSON files.

# How to run

# Functionalities 
### Menu
0. Reset configurations
1. Add new configuration
2. Display current configurations  
3. Update configurations  
4. Save configurations to a file  
5. Load configurations from a file  
6. Exit  

#### 0. Reset configurations
    Resets the current configurations.

#### 1. Add new configuration
    Asks the user to add a new configuration. First an input of the configuration's name and then an input of the configuration's parameters, using the specified format "key: value" separated by comma  
    Example:  
    "param1": value, "param2": value

#### 2. Display current configurations
    Displays to the user all the currently available configurations.

#### 3. Update configurations
    Asks the user for a configuration's name and allows them to update that specific configuration. The update forces the user to input configuration parameters separated by commas. 
    Example:  
    "param1: value, param2: value, param3: value"
    
#### 4. Save configurations to a file
    Asks the user for a file name to save the current configurations in a json format.

#### 5. Load configurations from a file 
    Asks the user for a file name which contains saved configurations in a json format.

#### 6. Exit
    Exits the application.

# Custom error messages
### Errors have custom messages to provide the user some guidance. 
These errors are:
- Trying to create a new configuration using an existing configuration's name
- When a new configuration's parameters don't follow the stipulated format
- Trying to update the configuration using a nonexistent configuration's name
- When updating the configuration's parameters don't follow the stipulated format
- Trying to load configurations from an invalid file