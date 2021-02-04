from prompt_state import PromptState

class DefenseState(PromptState):
    """
    State where the opponent is asked if he wants to defend
    from the player attack.
    """
    def __init__(self, player, opponent):
        super().__init__(player, opponent)
        self.help_text = self.help_text + help_text

    def run_initial_action(self):
        """
        As initial action, ask the opponent if he/she wants
        to defend or not.
        """
        # first check if oppontent has crests to defend
        if self.opponent.crest_pool.defense == 0:
            print(self.opponent.name + " has no defense " + \
                  "crests.")
            self.defend = False
            self.finish = True
        else:
            print(self.opponent.name + ", do you want " +
                  "to defend the attack? [y/n]")

    def parse_command(self, command):
        """
        Parse the command obtained from prompt.
        """
        # opponent defends
        if command.equals("y"):
            self.defend = True
            self.finish = True

        # opponent does not defend
        elif command.equals("n"):
            self.defend = False
            self.finish = True

        # generic commands
        else:
            super().parse_commands(command)

help_text = "\
Defense commands: \n\
    y: defend from player attack.\n\
    n: do not defend from player attack.\n\
"
