from duel_substate import DuelSubstate

class DungeonState(DuelSubstate):
    """
    State where player do actions on the dungeon, that is,
    move a monster, attack an opponent monster, or activate
    monster effects.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.help_text = self.help_text + help_text

    def set_new_start_message(self):
        """
        As new start print state title and crests and 
        monsters.
        """
        self.start_message  = "<DUNGEON PHASE> [f: finish]"
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

        # finish dungeon phase command
        if command.equals("f"):
            # decooldown monster
            self.duel.player.decooldown_monsters()

            # finish turn
            self.duel.advance_turn()
            self.next_state = self.roll_state
            self.next_state.set_start_message()

        # move command
        elif is_move_command(command): 
            subcommand = command.subcommand(1)
            self.run_move_command(subcommand)

        # attack command
        elif is_attack_command(command):
            self.run_attack_command(command)
        
        # generic commands
        else:
            super().update(command)

    def run_move_command(self, command):
        """
        Run command that makes a player monster to move in
        the dungeon.
        """
        # get tiles
        tile_i, tile_f = self.get_tiles(command)
        if not tile_i or not tile_f:
            return

        # get monster from origin tile and remove it
        content = tile_i.remove_content()
        if not content or not content.is_monster():
            self.log.add("No monster at origin.\n")
            return
        monster = content

        # put monster in destination tile
        success = tile_f.add_content(monster)
        if not success:
            self.log.add("Destination already occupied.")
        
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

    def get_tiles(self, command):
        """
        Get initial and final tiles from command. Used in 
        move and attack commands.
        """
        pos_i = Pos.from_string(command.list[0])
        pos_f = Pos.from_string(command.list[1])

        # check valid positions
        if not pos_i or not pos_f:
            return None, None

        # check positions in bound
        if not self.duel.dungeon.in_bound(pos_i):
            self.log.add("Origin out of bound.\n")
            return None, None
        if not self.duel.dungeon.in_bound(pos_f):
            self.log.add("Destination out of bound.\n")
            return None, None

        # check tiles are dungeon tiles
        tile_i = self.duel.dungeon.get_tile(pos_i)
        if not tile_i.is_dungeon():
            self.log.add("Origin is no dungeon path.\n")
            return None, None
        tile_f = self.duel.dungeon.get_tile(pos_f)
        if not tile_f.is_dungeon():
            self.log.add("Destination is no dungeon path.\n")
            return None, None

        return tile_i, tile_f

def is_move_command(command):
    """
    Check if command is a move command. NOTE: it does not 
    check if the pos strings are valid or in bound.
    """
    return command.len == 3 and command.equals_param(0, "m")

def is_attack_command(command):
    """
    Check if a command is an attack command, either and 
    attack to an opponent monster or to the dungeon master.
    """
    correct_len = 1 <= command.len <= 2
    return correct_len and command.are_params_int()

help_text = "\n\n\
Dungeon commands: \n\
    m xy1 xy2: monster at xy1 moves to position xy2\n\
    a xy1 xy2: monster at xy1 attacks monster at xy2\n\
    f        : finish phase."
