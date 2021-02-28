from duel_substate import DuelSubstate

class AttackState(DuelSubstate):
    """
    State where player can attack an opponent monster.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.help_text = self.help_text + help_text

    def set_new_start_message(self):
        """
        As new start print state title and crests and 
        monsters.
        """
        self.start_message  = "<ATTACK PHASE> [f: finish]"
        self.start_message += "\n\n"
        self.start_message += self.duel.dungeon.stringify()
        self.start_message += "\n\n"

    def set_start_message(self):
        """
        As start message print crests and monsters.
        """
        self.start_message  = self.duel.dungeon.stringify()
        self.start_message += "\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # default values for update
        self.next_state = self

        # finish attack phase command
        if command.equals("f"):
            # decooldown monster
            self.duel.player.decooldown_monsters()

            # finish turn
            self.duel.advance_turn()
            self.next_state = self.roll_state
            self.next_state.set_start_message()

        # attack command
        elif is_attack_command(command):
            self.run_attack_command(command)
        
        # generic commands
        else:
            super().update(command)
        
    def run_attack_command(self, command):
        """
        Run command that makes a player monster attack.
        """
        # get monster index
        i = command.list[0]

        # get player monster
        attacker = self.duel.player.prepare_attack(i)
        if not attacker:
            self.log.add("\n")
            return
            
        # distinguish between monster attack and ML attack
        if command.len == 2: # monster attack
            # get opponent monster
            i = command.list[1]
            attacked = self.duel.opponent.monster_list.get(i)
            if not attacked:
                self.log.add("\n")
                return
            
            # perform the attack
            self.attack_monster(attacker, attacked)

        else: # command.len == 1 (ML attack)            
            # perform the attack
            self.attack_monster_lord(attacker)

        self.next_state.set_start_message()

    def attack_monster(self, attacker, attacked):
        """
        Make attacker monster attack attacked monster.
        """
        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.duel.player.crest_pool.attack -= 1

        # inform the battle situation
        self.log.add(attacker.stringify_prebattle(attacked))
        self.log.add("\n")

        # if opponent has defense crests go to defense state
        if self.duel.opponent.crest_pool.defense > 0:
            self.next_state = self.def_state
            self.next_state.add_monsters(attacker, attacked)
            self.next_state.set_start_message()
            return

        # else perform the attack with no defense
        self.log.add(self.duel.opponent.name)
        self.log.add(" has no defense crests.\n")
        attacker.attack_monster(attacked, defending=False)

        # check if any of the monsters is dead
        self.duel.check_for_casualties()
        self.log.add("\n")

    def attack_monster_lord(self, attacker):
        """
        Make attacker monster attack the opponent monster 
        lord.
        """
        # check that opponent has no monster left
        if not self.duel.opponent.monster_list.is_empty():
            self.log.add("Cannot attack ML." + \
            "Opponent still has monsters left.\n")
            return

        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.duel.player.crest_pool.attack -= 1

        # do the attack
        attacker.attack_ml(self.duel.opponent)
        self.log.add("\n")

    #def stringify_state(self):
    #    """
    #    Create a string with relevant information in for the
    #    state.
    #    """
    #    s  = self.duel.player.name + " crests:\n"
    #    s += self.duel.player.crest_pool.stringify_short()
    #    s += "\n"
    #    s += self.duel.player.name + " monsters:\n"
    #    s += self.duel.player.monster_list.stringify()
    #    s += "\n\n"
    #    s += self.duel.opponent.name + " crests:\n"
    #    s += self.duel.opponent.crest_pool.stringify_short()
    #    s += "\n"
    #    s += self.duel.opponent.name + " monsters:\n"
    #    s += self.duel.opponent.monster_list.stringify()
    #    s += "\n\n"
    #    s +="Dungeon:\n"
    #    s += self.duel.dungeon.stringify()
    #    return s

def is_attack_command(command):
    """
    Check if a command is an attack command, either and 
    attack to an opponent monster or to the dungeon master.
    """
    correct_len = 1 <= command.len <= 2
    return correct_len and command.are_params_int()

help_text = "\n\n\
Attack commands: \n\
    #1 #2: player's monster #1 attacks opponent \n\
           monster's #2 \n\
    #    : player's monster # attacks opponent \n\
           dungeon master \n\
    f    : finish phase."
