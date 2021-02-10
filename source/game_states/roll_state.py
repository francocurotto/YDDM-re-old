from prompt_state import PromptState
from summon_state import SummonState

class RollState(PromptState):
    """
    State when player has to roll its dice hand.
    """
    def __init__(self, player, opponent):
        super().__init__(player, opponent)
        self.help_text = self.help_text + help_text

    def run_initial_action(self):
        """
        As inital action, print current player pool.
        """
        print("<ROLL PHASE>")
        print(self.player.stringify_pool())

    def parse_command(self, command):
        """
        Parse the command obtained by prompt. Return True if
        command is valid.
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
            return True

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
        # check if command is correct
        if not command.are_params_int():
            return False

        for i in command.list:
            result = self.player.add_dice_to_hand(i)
            if not result["success"]:
                print(result["message"])

        return True
        
    def run_getback_command(self, command):
        """
        Run command that get back a dice from dice hand to 
        the dice pool.
        """
        # check if command is correct
        if not command.are_params_int():
            return False

        # sort params in order to avoid IndexError in 
        # chopped list
        sorted_params = sorted(command.list, reverse=True)

        for i in sorted_params:
            result = self.player.dice_hand.remove_idx(i)
            if not result["success"]:
                print(result["message"])
        
        return True

    def parse_roll_command(self, command):
        """
        Distinguish between a normal roll command (no 
        paramenters) and a quick roll command (three int
        paramters). Return True if roll is successfull.
        """
        # normal roll
        if command.is_empty():
            self.run_roll_command()
            return True

        # quick roll command
        elif command.len == 3 and command.are_params_int():
            self.run_quick_roll_command(command)
            return True

        return False

    def run_roll_command(self):
        """
        Run command that roll dice hand. Must differenciate
        between roll command with or without int parameters.
        Return true if roll is successfull.
        """
        # Go, dice roll!
        result = self.player.roll_hand()
        
        if not result["success"]: # roll failed
            print(result["message"])
            return

        # roll succeded
        print("Roll result: " + result["string"])

        # check for summon
        dimensions = result["dimensions"]
        if not dimensions.is_empty():
            if not self.player.can_dimension():
                print(self.player.name + " reached " + \
                    "dimension limit.")
            else:
                summon_state = SummonState(self.player, 
                    self.opponent, dimensions)
                summon_state.start()

        # indicate that state is finished
        self.finish = True

    def run_quick_roll_command(self, command):
        """
        Add the three dice in command to dice hand and then
        run roll command. Return True if roll is successfull.
        """
        # add dice to dice hand
        indeces = command.list
        result = self.player.add_dice_to_hand_quick(*indeces)
        if not result["success"]:
            print(result["message"])

        # call run roll command without parameters
        self.run_roll_command()

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
