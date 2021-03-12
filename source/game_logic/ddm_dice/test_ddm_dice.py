"""
Script for testing a ddm dice object.
"""
import sys
sys.path.append("../summons")
import random
from ddm_dice_parser import DdmDiceParser

print("Welcome to the ddm dice test.\n\n\
Here you can create radom ddm dice from a database file and\n\
print their information.")

print("\n\
Input g to get a random ddm dice from the database.\n\
Input s to show current dice info.\n\
Input ss to show dice info in short form.\n\
Input q to quit.\n")

# create ddm dice list
parser = DdmDiceParser()
ddm_dice_list = parser.parse_ddm_dice("test_monsters.txt")

ddm_dice = None
while True:
    command = input(">")

    if command == "q":
        break
    
    if command == "g": # get ddm dice from database
        ddm_dice = random.choice(ddm_dice_list)
        print("dd dice obtained.\n")

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
