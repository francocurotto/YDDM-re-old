from duel_substate import DuelSubstate

class DefenseState(DuelSubtate):
    """
    State where the opponent is asked if he wants to defend
    from the player attack.
    """
    def __init__(self, player, opponent, attacker, attacked):
        super().__init__(player, opponent)
        self.attacker = attacker
        self.attacked = attacked
        self.help_text = self.help_text + help_text

    def run_message(self):
        """
        As initial action, ask the opponent if he/she wants
        to defend or not.
        """
        self.message  = self.opponent.name + ", do you want"
        self.message += " to defend the attack? [y/n]\n\n")

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
            self.opponent.crest_pool.defense -= 1
            self.attacker.attack_monster(self.attacked,  
                defend=True)

        # opponent does not defend
        elif command.equals("n"):
            self.attacker.attack_monster(self.attacked,  
                defend=True)

        # post attack actions
        self.message = attacker.message "\n"

        # check if any of the monsters is dead
        self.duel.check_for_casualties()
        self.message += self.duel.message + "\n\n"

        # define next state
        from attack_state import AttackState
        self.next_state = AttackState(self.duel)
        self.next_state.set_recurrent_message()

help_text = "\
Defense commands: \n\
    y: defend from player attack.\n\
    n: do not defend from player attack.\n\
"
