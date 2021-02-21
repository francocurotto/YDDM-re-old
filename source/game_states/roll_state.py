from duel_substate import DuelSubstate

class RollState(DuelSubstate):
    """
    State when player has to roll its dice hand.
    """
    def __init__(self, duel, next_turn=False):
        super().__init__(duel, next_turn)
        self.help_text = self.help_text + help_text

    def set_start_message(self):
        """
        As start message show player pool.
        """
        self.start_message  = self.player.name + " TURN\n"
        self.start_message += "<ROLL PHASE>\n"
        self.start_message += \
            self.player.stringify_pool() + "\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # default values for update
        self.next_state = self

        # add command
        if command.equals_param(0, "a"):
            subcommand = command.subcommand(1)
            self.run_add_command(subcommand)

        # get back command
        elif command.equals_param(0, "b"):
            subcommand = command.subcommand(1)
            self.run_getback_command(subcommand)

        # empty hand command
        elif command.equals("e"):
            self.player.empty_hand()
            self.log.add("\n")

        # roll command
        elif command.equals_param(0, "r"):
            subcommand = command.subcommand(1)
            self.run_roll_command(subcommand)

        # generic commands
        else:
            super().update(command)

    def run_add_command(self, command):
        """
        Run command that add a dice from dice pool to dice
        hand.
        """
        # check if command is correct
        if not command.are_params_int():
            return

        for i in command.list:
            self.player.add_dice_to_hand(i)

        self.log.add("\n")
        
    def run_getback_command(self, command):
        """
        Run command that get back a dice from dice hand to 
        the dice pool.
        """
        # check if command is correct
        if not command.are_params_int():
            return

        # sort params in order to avoid IndexError in 
        # chopped list
        sorted_params = sorted(command.list, reverse=True)

        for i in sorted_params:
            self.player.dice_hand.remove_idx(i)
        
        self.log.add("\n")

    def run_roll_command(self, command):
        """
        Distinguish between a normal roll command (no 
        paramenters) and a quick roll command (three int
        paramters).
        """
        # normal roll
        if command.is_empty():
            self.run_normal_roll_command()

        # quick roll command
        elif command.len == 3 and command.are_params_int():
            self.run_quick_roll_command(command)

        self.log.add("\n")

    def run_normal_roll_command(self):
        """
        Run command that roll dice hand.
        """
        # Go, dice roll!
        roll_result = self.player.roll_hand()
        dimensions = roll_result.dimensions

        if not roll_result.sides: # roll failed
            return

        # roll succeded
        self.log.add("GO DICE ROLL!\n")
        self.log.add(roll_result.stringify_sides() + "\n")

        # define next state
        if self.can_dimension(dimensions): # dimension able
            self.dim_state.dimensions = dimensions
            self.next_state = self.dim_state

        else: # dimension unable
            self.next_state = self.attack_state

        self.next_state.set_start_message()

    def run_quick_roll_command(self, command):
        """
        Add the three dice in command to dice hand and then
        run roll command.
        """
        # add dice to dice hand
        idxs = command.list
        success = self.player.add_dice_to_hand_quick(*idxs)
        if not success:
            return

        # call run roll command without parameters
        self.run_normal_roll_command()

    def can_dimension(self, dimensions):
        """
        Check if current player can dimension after roll.
        """
        # no dimension in roll
        if dimensions.is_empty():
            return False

        # hit maximum number of dimensions
        elif self.player.hit_dimension_limit():
            self.log.add(self.player.name + " reached " + \
                "dimension limit.\n")
            return False

        # dimension possible
        return True

help_text = "\n\n\
Hand commands: \n\
    a # [# #]: add 1/2/3 dice from dice pool at positions \n\
               # to dice hand \n\
    b # [# #]: get back 1/2/3 dice from hand at positions \n\
               # from dice hand to dice pool \n\
    e        : empty hand \n\
    r        : roll dice hand \n\
    r # # #  : ignore current dice at dice hand and \n\
               roll dice at positions # # # \n\
               (quick roll)"
