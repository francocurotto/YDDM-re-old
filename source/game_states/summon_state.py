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
        print("Available summons:")
        print(self.dimensions.stringify())
        print("Select with number [s: skip].")

    def parse_command(self, command):
        """
        Parse command obtained by prompt.
        """
        # print available summons command
        if command.equals("p", "as"):
            print(self.dimensions.stringify())
            return False

        if command.equals("s"):
            print("")
            return True

        # dimension dice
        if command.len == 1 and command.is_int(0):
            i = command.list[0]
            result = self.dimensions.get(i)
            if not result["success"]:
                print(result["message"])
                return False

            self.player.dimension_dice(result["item"])
            print("")
            return True

        # generic commands
        return super().parse_command(command)

help_text = "\
Summon commands: \n\
    p as: print available summons \n\
    s   : skip dimension \n\
    #   : dimension dice \n\
"
