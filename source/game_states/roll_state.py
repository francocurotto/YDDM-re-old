from duel_substate import DuelSubtate
from summon_state import SummonState

class RollState(DuelSubstate):
    """
    State when player has to roll its dice hand.
    """
    def __init__(self, player, opponent):
        super().__init__(player, opponent)
        self.help_text = self.help_text + help_text

    def initial_message(self):
        """
        As initial message: current player pool.
        """
        message = "<ROLL PHASE>\n" + \
            self.player.stringify_pool() + "\n\n"

    def update(self, command):
        """
        Update state given command. Return result dictionary
        with the necessary information for parent state.
        """
        # add command
        if command.equals_param(0, "a"):
            subcommand = command.subcommand(1)
            return self.run_add_command(subcommand)

        # get back command
        elif command.equals_param(0, "b"):
            subcommand = command.subcommand(1)
            return self.run_getback_command(subcommand)

        # empty hand command
        elif command.equals("e"):
            self.player.empty_hand()
            result = self.default_result()
            result["message"] = "\n"
            return result

        # roll command
        elif command.equals_param(0, "r"):
            subcommand = command.subcommand(1)
            return self.parse_roll_command(subcommand)

        # generic commands
        else:
            return super().parse_command(command)

    def run_add_command(self, command):
        """
        Run command that add a dice from dice pool to dice
        hand.
        """
        result = self.default_result()

        # check if command is correct
        if not command.are_params_int():
            return result

        for i in command.list:
            add_result = self.player.add_dice_to_hand(i)
            if not add_result["success"]:
                message = add_result["message"]
                result["message"] += message + "\n"

        result["message"] += "\n"
        return result
        
    def run_getback_command(self, command):
        """
        Run command that get back a dice from dice hand to 
        the dice pool.
        """
        result = self.default_result()

        # check if command is correct
        if not command.are_params_int():
            return result

        # sort params in order to avoid IndexError in 
        # chopped list
        sorted_params = sorted(command.list, reverse=True)

        for i in sorted_params:
            rem_result = self.player.dice_hand.remove_idx(i)
            if not rem_result["success"]:
                message = rem_result["message"]
                result["message"] += message + "\n"
        
        result["message"] += "\n"
        return result

    def parse_roll_command(self, command):
        """
        Distinguish between a normal roll command (no 
        paramenters) and a quick roll command (three int
        paramters). Return True if roll is successfull.
        """
        # normal roll
        if command.is_empty():
            return self.run_roll_command()

        # quick roll command
        elif command.len == 3 and command.are_params_int():
            return self.run_quick_roll_command(command)

        # invalid command
        return self.default_result()

    def run_roll_command(self):
        """
        Run command that roll dice hand. Must differenciate
        between roll command with or without int parameters.
        Return true if roll is successfull.
        """
        result = self.default_result()

        # Go, dice roll!
        roll_result = self.player.roll_hand()
        
        if not roll_result["success"]: # roll failed
            result["message"] = roll_result["message"] + "\n"
            return result

        # roll succeded
        result["message"] = "Roll result: " + \
            roll_result["string"] + "\n"

        # check for summon
        dimensions = roll_result["dimensions"]
        dim_result = self.can_dimension(dimensions)

        if dim_result["success"]: # dimension able
            next_state = SummonState(self.player, self.
                opponent, dimensions)
            message = ""
            message2 = next_state.initial_message()

        else: # dimension unable
            next_state = AttackState(self.player, self.
                opponent)
            message += dim_result["message"]
            message2 = next_state.initial_message()

        # generate result
        result["nextstate"] = next_state
        result["message"] += message + "\n"
        result["message2"] = message2

        return result

    def run_quick_roll_command(self, command):
        """
        Add the three dice in command to dice hand and then
        run roll command. Return True if roll is successfull.
        """
        result = self.default_result()

        # add dice to dice hand
        indeces = command.list
        add_result = self.player.add_dice_to_hand_quick(
            *indeces)
        if not roll_result["success"]:
            result["message"] = add_result["message"]
            return result

        # call run roll command without parameters
        return self.run_roll_command()

    def can_dimension(self, dimensions):
        """
        Check if current player can dimension after roll.
        """
        result = {}
        if dimensions.is_empty(): # no dimensions in roll
            result["success"] = False
            result["message"] = ""

        elif self.player.hit_dimension_limit(): # hit max dim
            result["success"] = False
            result["message"] = self.player.name + \
                " reached dimension limit.\n")

        else: # dimension possible
            result["success"] = True

        return result

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
