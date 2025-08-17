import initializer as init
import advance as adv
import console as con

from pyautogui import hotkey as key
from os import *
from sys import exit

key('F11')
init.clear()
system("color c")
print(f"Welcome to the {init.name} os!")

def run(id):
    x = adv.Console()
    cb = con.CBrowse
    match id:
        case "1":
            x.change_color(input("Enter text color >>> ") or "")
            init.clear()
            select_action()
        #case "2":
        #    x.set_name(input("Insert name >>> "))
        #    init.clear()
        #    print(f'Name set as {init.name}')
        #    select_action()
        case "2":
            cb.file_browser()
            init.clear()
            select_action()
        case "3":
            x.run_console()
            init.clear()
            select_action()
        case "4":
            exit()
        case _:
            print("Action doesn't exist.")
            init.clear()
            select_action()

def select_action():
    init.createspace()
    print("What would you like to do?")
    for id, element in enumerate(init.actions):
        print(f"{id+1}. {element}")
    init.createspace()
    run(init.choose())


x=select_action()
run(x)

input()