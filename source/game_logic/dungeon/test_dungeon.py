import sys
sys.path.append("../..")
sys.path.append("../../functions")
sys.path.append("../game_states")
sys.path.append("../ddm_list")
sys.path.append("../ddm_dice")
sys.path.append("../dungeon_objects")
sys.path.append("../player")

import settings
from logger import Logger
from duel import Duel
from dungeon import Dungeon
from dice_nets.pos import Pos
from dice_nets.dice_net import create_net
from dungeon_object import DungeonObject

#settings.print_type = "ascii"
#settings.print_type = "unicode"
settings.print_type = "emoji"
settings.library_path = "../" + settings.library_path

log = Logger()
settings.library_path = "../../databases/library.yaml"
duel = Duel("","",log)
dungeon = Dungeon(duel.players, log)

i = False
while True:
    # get player
    player = duel.players[i]

    print(dungeon.stringify() + "\n")
    command = input("Add a net <net> <xy> <trans> ")
    if command == "q":
        break
    command_list = command.split()
    if len(command_list) < 2:
        continue

    # get net
    dice_net = create_net(command_list[0], log)
    if not dice_net:
        continue
    # get pos
    pos = Pos.from_string(command_list[1])
    if not pos:
        continue

    # apply transformations
    trans_list = command_list[2:]
    success = dice_net.apply_trans(trans_list)
    if not success:
        print(log.flush())
        continue 

    dungeon.set_net(dice_net, pos, player, DungeonObject())
    print(log.flush())

    # update index
    i = not i
