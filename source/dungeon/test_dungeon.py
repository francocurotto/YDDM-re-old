import sys
sys.path.append("..")
sys.path.append("../game_states")
from colorama import Fore

import settings
from functions import color
from logger import Logger
from dungeon import Dungeon
from pos import Pos
from dungeon_tile import DungeonTile

#settings.print_type = "ascii"
#settings.print_type = "unicode"
settings.print_type = "emoji"

log = Logger()
dungeon = Dungeon(log)

# choose char
if settings.print_type == "ascii":
    char = color("[]", Fore.BLUE)
elif settings.print_type == "unicode":
    char = color("ロ", Fore.BLUE)
elif settings.print_type == "emoji":
    char = "🟦"

while True:
    print(dungeon.stringify() + "\n")
    command = input("Add a tile at <xy> ")
    if command == "q":
        break
    pos = Pos.from_string(command)
    if not pos:
        continue

    # create tile
    dungeon_tile = DungeonTile(char)
    dungeon.add_dungeon_tile(dungeon_tile, pos)
    print(log.flush())
