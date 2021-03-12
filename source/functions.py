####################
# Module Functions #
####################
import os
def get_all_modules():
    """
    Get all the possible existing modules starting from 
    current path.
    """
    # get all folders starting from current path
    dirlist = [dirtuple[0] for dirtuple in os.walk(".")]
    # remove invalid module folders
    modlist = [] 
    for dirname in dirlist: 
        if not dirname.endswith("/__pycache__"):
            modlist.append(dirname)
    return modlist

###################
# Color Functions #
###################
from colorama import Fore, Back, Style

color_fg_dict = {
    "black"   : Fore.BLACK,
    "red"     : Fore.RED,
    "green"   : Fore.GREEN, 
    "yellow"  : Fore.YELLOW, 
    "blue"    : Fore.BLUE,  
    "magenta" : Fore.MAGENTA, 
    "cyan"    : Fore.CYAN,  
    "white"   : Fore.WHITE}  

color_bg_dict = {
    "black"   : Back.BLACK,
    "red"     : Back.RED,
    "green"   : Back.GREEN, 
    "yellow"  : Back.YELLOW, 
    "blue"    : Back.BLUE,  
    "magenta" : Back.MAGENTA, 
    "cyan"    : Back.CYAN,  
    "white"   : Back.WHITE}  

def color_fg(string, color):
    """
    Adds color to string at foreground. Color must be a key
    from color_fg_dict dictionary.
    """
    return color_fg_dict[color] + string + Style.RESET_ALL

def color_bg(string, color):
    """
    Adds color to string at background. Color must be a key 
    from color_bg_dict dictionary.
    """
    return color_bg_dict[color] + string + Style.RESET_ALL

def grayout(s):
    """
    Grays out string s.
    """
    return Fore.BLACK + Style.BRIGHT + s + Style.RESET_ALL
