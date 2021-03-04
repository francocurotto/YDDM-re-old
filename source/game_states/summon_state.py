from duel_substate import DuelSubstate

class SummonState(DuelSubstate):
    """
    State when player choose the dice monster/item to summon 
    after a roll.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.dimensions = None
        self.help_text = self.help_text + help_text

    def restart(self):
        """
        Restart state.
        """
        # reset next state
        self.next_state = self

        # set start message
        self.start_message  = "Available summons:\n"
        self.start_message += \
            self.dimensions.stringify() + "\n"
        self.start_message += \
            "Select with number [s: skip].\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # print available summons command
        if command.equals("p", "as"):
            self.log.add(self.dimensions.stringify())
            self.log.add("\n\n")

        # skip summon and go to next state
        elif command.equals("s"):
            self.log.add("\n")
            self.next_state = self.dun_state
            self.next_state.set_new_start_message()

        # dice summon
        elif command.len == 1 and command.is_int(0):
            # get dice to summon
            i = command.list[0]
            dice = self.dimensions.get(i)
            if not dice:
                self.log.add("\n")
                return

            # define next state
            self.next_state = self.dim_state
            self.next_state.dice = dice
            self.next_state.restart()

        # generic commands
        else:
            super().update(command)

help_text = "\n\n\
Summon commands: \n\
    p as: print available summons \n\
    s   : skip summon \n\
    #   : summon dice"
