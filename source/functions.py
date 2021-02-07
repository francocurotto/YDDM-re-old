# color functioins
from colorama import Fore, Style

def color(s, c):
    """
    Adds color c to string s. Assumes colors from the 
    colorama package.
    """
    return c + s + Style.RESET_ALL

def grayout(s):
    """
    Grays out string s.
    """
    return Fore.BLACK + Style.BRIGHT + s + Style.RESET_ALL
