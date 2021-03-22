"""
Script for testing a ddm dice object.
"""
import sys
sys.path.append("../..")
sys.path.append("../../functions")
sys.path.append("../dungeon_objects")
sys.path.append("../ddm_list")
sys.path.append("../game_states")
import random
from dice_list import DiceList
from logger import Logger

print("Welcome to the ddm dice test.\n\n\
Here you can create radom ddm dice from a database file and\n\
print their information.")

print("\n\
Input g to get a random ddm dice from the database.\n\
Input s to show current dice info.\n\
Input ss to show dice info in short form.\n\
Input q to quit.\n")

# create ddm dice list
log = Logger()
ddm_dice_list = DiceList("library", log)
ddm_dice_list.fill_from_library("../../databases/library.yaml")

ddm_dice = None
while True:
    command = input(">")

    if command == "q":
        break
    
    if command == "g": # get ddm dice from database
        ddm_dice = random.choice(ddm_dice_list.list)
        print("ddm dice obtained.\n")

    if command == "s":
        if ddm_dice is None:
            print("No ddm dice obtained yet.\n")
            continue
        print(ddm_dice.stringify()+"\n")

    if command == "ss":
        if ddm_dice is None:
            print("No ddm dice obtained yet.\n")
            continue
        print(ddm_dice.stringify_short()+"\n")

print("\nBye!")
