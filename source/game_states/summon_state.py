from duel_substate import DuelSubstate
#from attack_state import AttackState

class SummonState(DuelSubstate):
    """
    State when player summon a monster/item after a roll.
    """
    def __init__(self, player, opponent, dimensions):
        super().__init__(player, opponent)
        self.dimensions = dimensions
        self.help_text = self.help_text + help_text
        self.message = ""

    def set_initial_message(self):
        """
        As intial message: available dimensions.
        """
        self.message  = "Available summons:\n"
        self.message += self.dimensions.stringify() + "\n"
        self.message += "Select with number [s: skip].\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # default values for update
        from roll_state import RollState
        self.next_state = SummonState(self.player, 
            self.opponent, self.dimensions)
        self.message = ""

        # print available summons command
        if command.equals("p", "as"):
            self.message  = self.dimensions.stringify()
            self.message += "\n\n"

        # skip dimension and go to next state
        elif command.equals("s"):
            #self.next_state = AttackState(self.player, 
            #    self.opponent)
            self.next_state = RollState(self.opponent, 
                self.player)
            self.next_state.set_initial_message()
            self.message = "\n"

        # dice dimension
        elif command.len == 1 and command.is_int(0):
            # get dice to dimension
            i = command.list[0]
            dice = self.dimensions.get(i)
            if not dice:
                self.message  = self.dimensions.message
                self.message +="\n\n"
                return

            # dimension the dice!
            self.player.dimension_dice(dice)

            # define next state
            self.next_state = RollState(self.opponent, 
                self.player)
            self.next_state.set_initial_message()
            self.message = "DIMENSION THE DICE!\n\n"

        # generic commands
        else:
            return super().parse_command(command)

help_text = "\n\n\
Summon commands: \n\
    p as: print available summons \n\
    s   : skip dimension \n\
    #   : dimension dice"
