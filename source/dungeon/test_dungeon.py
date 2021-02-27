import sys, glob
sys.path.append("..")
dirlist = glob.glob("../*/")
dirlist.remove("../__pycache__/")
for dirname in dirlist:
    sys.path.append(dirname)

import settings
from logger import Logger
from duel import Duel
from dungeon import Dungeon
from dice_nets.pos import Pos
from dice_nets.net_x1 import NetX1

#settings.print_type = "ascii"
#settings.print_type = "unicode"
settings.print_type = "emoji"
settings.library_path = "../" + settings.library_path

log = Logger()
duel = Duel(log)
dungeon = Dungeon(duel.players, log)
player = duel.players[0]

while True:
    print(dungeon.stringify() + "\n")
    command = input("Add a tile at <xy> ")
    if command == "q":
        break
    command_list = command.split()

    # split command
    pos = Pos.from_string(command_list[0])
    trans_list = command_list[1:]
    if not pos:
        continue

    # create net
    dice_net = NetX1(log)

    # apply transformations
    success = dice_net.apply_trans(trans_list)
    if not success:
        print(log.flush())
        continue 

    dungeon.set_net(dice_net, pos, player, None)
    print(log.flush())
