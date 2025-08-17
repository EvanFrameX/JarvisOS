import initializer as initi
from console import *

from os import *
from colorama import *

init()

class Console(CBrowse):
    def __init__(self):
        pass
    
    def change_color(self, main: str):
        try:
            print(eval(f'Fore.{main.upper()}'))
        except AttributeError as ae:
            system(f'color {main}')
    
    def set_name(self, x: str):
        if input("Warning: You'll change the name of the OS. Do you wanna continue? (Y/N) >>> ").lower == "n":
            return
        
    def run_console(self):
        x = True
        while x:
            command = input("$ >>> ")
            if command != "SystemReturn":
                system(f"{command}")
            else:
                x = False
