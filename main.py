# Menu navigation with the different functionalities
# The menu's input is handled by input_handler.py

# Menu:
#   1. Add new configuration
#   2. Display current configurations  
#   3. Update configurations  
#   4. Save configurations to a file  
#   5. Load configurations from a file  
#   6. Exit  
from utils.error_handling import *
from utils.input_handler import Menu

if __name__=="__main__":
    Menu.menu()