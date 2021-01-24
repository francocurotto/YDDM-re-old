from prompt_state import PromptState

class SummonState(PromptState):
    """
    State when player summon a monster/item after a roll.
    """
    def __init__(self, player, opponent, dimensions):
        super().__init__(player, opponent)
        self.dimensions = dimensions
        self.help_text = self.help_text + help_text

    def run_initial_action(self):
        """
        As intial action, print available dimensions.
        """
        print(self.dimensions.stringify())

    def parse_command(self, command):
        """
        Parse command obtained by prompt.
        """
        # generic commands
        super().parse_commands(command)

        # print available summons command
        if command.equals("p", "s"):
            print(self.dimensions.stringify())
            return False

        # dimension dice
        if command.len == 1 and command.is_int(0):
            i = command.list[0]
            result = self.dimensions.get_dice(i)
            if not result["success"]
                print(result["message"])
                return False

            self.player.dimension_dice(result["dice"])
            return True

help_text = "\
Summon commands: \n\
    p s: print available summons \n\
    #  : dimension dice \n\
\n"
