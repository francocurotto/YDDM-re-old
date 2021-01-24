from prompt_state import PromptState

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
        print(self.player.stringify_pool())

    def parse_command(self, command):
        """
        Parse the command obtained from prompt.
        """
        # generic commands
        super().parse_command(command)

        # add command
        elif command.equals_param(0, "a"):
            subcommand = command.subcommand(1)
            self.run_add_command(subcommand)
            return False

        # get back command
        elif command.equals_param(0, "b"):
            subcommand = command.subcommand(1)
            self.run_getback_command(subcommand)
            return False

        # roll command
        elif command.equals_param("r"):
            subcommand = command.subcommand(1)
            success = self.parse_roll_command(subcommand)
            return success

    def run_add_command(command):
        """
        Run command that add a dice from dice pool to dice
        hand.
        """
        # check if command is correct
        if not command.are_params_int():
            return

        for i in command.list:
            result = self.player.add_dice_to_hand(i)
            if not result["success"]:
                print(result["message"])
        
        print("")

    def run_getback_command(command):
        """
        Run command that get back a dice from dice hand to 
        the dice pool.
        """
        # check if command is correct
        if not command.are_params_int():
            return

        # sort params in order to avoid IdexError in 
        # chopped list
        sorted_params = sorted(command.list)

        for i in sorted_params:
            result = player.dice_hand.remove_dice_idx(i)
            if not result["success"]:
                print(result["message"])

        print("")
        
    def parse_roll_command(command):
        """
        Distinguish between a normal roll command (no 
        paramenters) and a quick roll command (three int
        paramters).
        """
        # normal roll
        if command.is_empty():
            return self.run_roll_command()

        # quick roll command
        if command.len == 3 and command.are_params_int():
            return self.run_quick_roll_command(command)

        # invalid command
        return False

    def run_roll_command(command):
        """
        Run command that roll dice hand. Must differenciate
        between roll command with or without int parameters.
        """
        # Go, dice roll!
        result = self.player.roll_hand()
        
        if not result["success"]: # roll failed
            print(result["message"] + "\n")
            return False

        # roll succeded
        print("Roll result:" + result["string"] + "\n")

        # check for summon
        dimensions = result["dimensions"]
        if not dimensions.is_empty():
            summon_state = SummonState(self.player, 
                self.opponent)
            summon_state.start(player, dimensions)

        return True

    def run_quick_roll_command(command):
        """
        Add the three dice in command to dice hand and then
        run roll command.
        """
        # add dice to dice hand
        indeces = command.list
        result = self.player.add_dice_to_hand_quick(*indeces)
        if not result["success"]:
            print(result["message"])
            return False

        # call run roll command without parameters
        command = command.subcommand(0,1)
        return self.run_roll_command(command)

help_text = "\
Hand commands: \n\
    a # [# #]: add 1/2/3 dice from dice pool at positions \n\
               # to dice hand \n\
    b # [# #]: get back 1/2/3 dice from hand at positions \n\
               # from dice hand to dice pool \n\
    r        : roll dice hand \n\
    r # # #  : ignore current dice at dice hand and \n\
               roll dice at positions # # # \n\
               (quick roll) \n\
\n"
