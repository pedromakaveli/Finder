import os
from colorama import init, Fore, Back, Style
from time import sleep

init()

class Objeto:
    #-----------------------------------------------------------------------------
    # This variables are passed by a instance locate on the end of this code
    currentExtension = ''
    currentPath = os.getcwd()
    filesPath = []
    #-----------------------------------------------------------------------------

# Here we find the main menu

class Main:
    ...