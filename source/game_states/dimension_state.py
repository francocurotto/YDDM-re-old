from duel_substate import DuelSubstate
from dice_nets.dice_net import create_net
from dice_nets.pos import Pos

class DimensionState(DuelSubstate):
    """
    State when player choose where to dimension the dice
    after a roll.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.dungeon = self.duel.dungeon
        self.dice_net = None
        self.pos = None
        self.help_text = self.help_text + help_text

    def restart(self):
        """
        Restart state.
        """
        # reset next state
        self.next_state = self

        # set start message
        self.start_message  = "Dimension Dice. "
        self.start_message += "Net types: [s: skip]\n"
        self.start_message += self.get_net_string()
        self.start_message += "\n\n"
        self.start_message += self.duel.dungeon.stringify()
        self.start_message += "\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # skip dimension and go to next state
        if command.equals("s"):
            self.log.add("\n")
            self.next_state = self.dun_state
            self.next_state.restart_new()

        # dice dimension
        elif self.check_dimension_command(command):
            # dimension the dice!
            summon = self.duel.player.summon_dice(self.dice)
            success = self.dungeon.set_net(self.dice_net, 
                self.pos, self.duel.player, summon)
            if not success:
                self.log.add("\n")
                return

            # define next state
            self.log.add("DIMENSION THE DICE!\n\n")
            self.next_state = self.dun_state
            self.next_state.restart_new()

        # generic commands
        else:
            super().update(command)

    def check_dimension_command(self, command):
        """
        Check if command is a valid dimension command. NOTE:
        It does not check if the dimension itself is valid,
        just that the command make sense.
        """
        # check command length first:
        if command.len < 2:
            return False

        # get command items
        net_str = command.list[0]
        pos_str = command.list[1]
        trans_list = command.list[2:]

        # get net
        self.dice_net = create_net(net_str, self.log)
        if not self.dice_net:
            return False
    
        # get pos
        self.pos = Pos.from_string(pos_str)
        if not self.pos:
            return False

        # apply transformations
        success = self.dice_net.apply_trans(trans_list)
        if not success:
            return False

        return True

    def get_net_string(self):
        """
        Creates a string showing all possible nets and their
        names.
        """
        # get normal tile char
        tile_char = self.duel.player.chars["tile"]
        
        # get center tile char
        summon = self.dice.card.summon(
            self.duel.player.chars, self.log)
        center_char = summon.tile_char

        # create net string from base net string
        net_str = base_net_str.replace("[]", tile_char)
        net_str = net_str.replace("()", center_char)

        return net_str

base_net_str = "\
  T1     T2     Z1     Z2     X1     X2   \n\
[][][] [][]   [][]   [][]     []     []   \n\
  ()     ()[]   ()     ()   []()[] []()   \n\
  []     []     []     [][]   []     [][] \n\
  []     []     [][]   []     []     []   \n\
                                          \n\
  M1   M2     S1     S2     L1            \n\
[][]   []     []     []     []            \n\
  ()   []()   []()[] []()   []            \n\
  [][]   [][]   []     [][] ()[]          \n\
    []     []   []     []     []          \n\
                              []"

help_text = "\n\n\
Dimension commands: \n\
    s : skip dimensions \n\
    <net> <yx> <trans> : command to dimension de dice.\n\
        <net>   : one of the 11 possible dice nets.\n\
        <yx>    : coordinates for the center of the net.\n\
        <trans> : transformation to apply to the net\n\
                  before dimension, they can be 0 or more\n\
                  of the following:\n\
            - tcw  : turn net clock-wise 90 degrees\n\
            - tccw : turn net counter clock-wise 90 degrees\n\
            - flr  : flip net horizontally (left-right)\n\
            - fud  : flip net vertically (left-right)"
