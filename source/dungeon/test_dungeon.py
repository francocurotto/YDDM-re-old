import sys
sys.path.append("..")
sys.path.append("../game_states")
from colorama import Fore

import settings
from functions import color
from logger import Logger
from dungeon import Dungeon, Pos
from dungeon_tile import DungeonTile

settings.print_type = "ascii"
#settings.print_type = "unicode"

log = Logger()
dungeon = Dungeon(log)
char = color("[]", Fore.BLUE)

while True:
    print(dungeon.stringify() + "\n")
    command = input("Add a tile at <xy> ")
    if command == "q":
        break
    pos = Pos(command)
    if not pos.valid:
        continue

    # create tile
    dungeon_tile = DungeonTile(char)
    dungeon.add_dungeon_tile(dungeon_tile, pos)
    print(log.flush())

