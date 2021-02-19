from duel_substate import DuelSubstate
from roll_state import RollState
from defense_state import DefenseState

class AttackState(DuelSubstate):
    """
    State where player can attack an opponent monster.
    """
    def __init__(self, duel, next_turn= False):
        super().__init__(duel, next_turn)
        self.help_text = self.help_text + help_text

    def initial_message(self):
        """
        As initial message print player and opponent 
        summons.
        """
        self.message  = "<ATTACK PHASE> [f: finish]\n"
        self.message +=  self.stringify_state() + "\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # default values for update
        self.next_state = AttackState(self.duel)
        self.message = ""

        # finish attack phase command
        if command.equals("f"):
            self.next_state = RollState(self.duel, True)
            self.next_state.set_initial_message()

        # attack command
        elif is_attack_command(command):
            self.run_attack_command(command)
        
        # generic commands
        else:
            super().parse_command(command)
        
    def run_attack_command(self, command):
        """
        Run command that makes a player monster attack.
        """
        # get monster index
        i0 = command.list[0]

        # get player monster
        attacker = self.player.prepare_attack(i0)
        if not attacker:
            self.message = self.player.message
            return
            
        # distinguish between monster attack and ML attack
        if command.len == 2: # monster attack
            # get opponent monster
            i1 = command.list[1]
            monster = self.opponent.monster_list.get(i1)
            if not monster:
                self.message = self.opponent.monster_list.\
                    message
                return
            
            # perform the attack
            self.attack_monster(attacker, attacked)

        else: # command.len == 1 (ML attack)            
            # perform the attack
            self.attack_monster_lord(attacker)

        # print state info
        print("")
        print(self.stringify_state())

    def attack_monster(self, attacker, attacked):
        """
        Make attacker monster attack attacked monster.
        """
        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.player.crest_pool.attack -= 1

        # inform the battle situation
        print(attacker.stringify_prebattle(attacked))

        # then get defense flag
        defense_state = DefenseState(self.player, 
            self.opponent)
        defense_state.start()
        defend = defense_state.defend

        # do the attack
        message = attacker.attack_monster(attacked, defend)
        print(message)

        # check if any of the monsters is dead
        message = self.player.check_for_casualties()
        if message:
            print(message)
        message = self.opponent.check_for_casualties()
        if message:
            print(message)

    def attack_monster_lord(self, attacker):
        """
        Make attacker monster attack the opponent monster 
        lord.
        """
        # check that opponent has no monster left
        if not self.opponent.monster_list.is_empty():
            print("Cannot attack ML. Opponent still has " +
                "monsters left.")
            return

        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.player.crest_pool.attack -= 1

        # do the attack
        message = attacker.attack_ml(self.opponent)
        print(message)

    def stringify_state(self):
        """
        Create a string with relevant information in for the
        state.
        """
        string  = self.player.name + " crests:\n"
        string += self.player.crest_pool.stringify_short()
        string += "\n"
        string += self.player.name + " monsters:\n"
        string += self.player.monster_list.stringify()
        string += "\n\n"
        string += self.opponent.name + " crests:\n"
        string += self.opponent.crest_pool.stringify_short()
        string += "\n"
        string += self.opponent.name + " monsters:\n"
        string += self.opponent.monster_list.stringify()
        return string 

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
