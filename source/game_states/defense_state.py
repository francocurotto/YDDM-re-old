from duel_substate import DuelSubstate

class DefenseState(DuelSubstate):
    """
    State where the opponent is asked if he wants to defend
    from the player attack.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.help_text = self.help_text + help_text

    def set_start_message(self):
        """
        As start message ask the opponent if he/she wants
        to defend or not.
        """
        self.start_message  = self.duel.opponent.name
        self.start_message += ", do you want to defend the "
        self.start_message += "attack? [y/n]\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # defense command
        if command.equals("y") or command.equals("n"):
            self.run_defense_command(command)

        # generic commands
        else:
            super().update(command)

    def run_defense_command(self, command):
        """
        Run command were a desition between defending or not
        was taken.
        """
        # opponent defends
        if command.equals("y"):
            self.duel.opponent.crest_pool.defense -= 1
            self.attacker.attack_monster(self.attacked,  
                defending=True)

        # opponent does not defend
        elif command.equals("n"):
            self.attacker.attack_monster(self.attacked,  
                defending=False)

        # check if any of the monsters is dead
        self.duel.check_for_casualties()
        self.log.add("\n")

        # define next state
        self.next_state = self.atk_state
        self.next_state.set_start_message()

    def add_monsters(self, attacker, attacked):
        """
        Add the participant monster to the state.
        """
        self.attacker = attacker
        self.attacked = attacked

help_text = "\
Defense commands: \n\
    y: defend from player attack.\n\
    n: do not defend from player attack.\n\
"
