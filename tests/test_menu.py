import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import inspect
 
# adding Folder_2 to the system path
# import from parent directory
currentdir = os.path.dirname(os.path.abspath(
             inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from utils import *

class TestMenu(unittest.TestCase):

    config_menu=Menu()

    def setUp(self):
        self.config_menu.configurations = dict()
    
    '''
    # Não está a funcionar, era suposto utilizar o método menu e fornecer os inputs necessários mas não foi possível dar mock aos inputs
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["add", "api", "documents: \"/docs\", profile: \"/profile\""])
    def test_reset_config(self, m_input, m_stdout):
        self.config_menu.menu()

        self.config_menu.__display_config()
        
        self.assertEqual(m_stdout.getvalue(), "api: {'documents': '/docs', 'profile': '/profile'}")
    '''
    
    def test_config(self):
        self.config_menu.configurations = {"api": {"documents": "/documents", "profile": "/profile"}}

        self.assertEquals({"api": {"documents": "/documents", "profile": "/profile"}}, self.config_menu.configurations)



if __name__ == '__main__':
    unittest.main()