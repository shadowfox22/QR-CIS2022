from os import *

def cl():

    # WINDOWS CLIENTS
    if name == 'nt':
        _ = system('cls')

    # UNIX CLIENTS
    if name == 'posix':
        _ = system('clear')