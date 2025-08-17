import colorama
from sys import platform
from os import system

colorama.init()

name="Jarvis+"
actions=["change color", "browse files/folders", "run console", "exit"]

def createspace():
    print("")
def choose():
    return input(">>>")
def clear():
    system(f'{'cls' if platform.startswith('win') else 'clear'}')