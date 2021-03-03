from duel_substate import DuelSubstate
from dice_nets.pos import Pos

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
        # 1. get tiles
        tile_i, tile_f = self.get_tiles(command)
        if not tile_i or not tile_f:
            return

        # 2. get monster
        player = self.duel.player
        monster = self.get_player_monster(tile_i)
        if not monster:
            return

        # 3. check that monster hasn't move yet
        if monster.move_cooldown:
            self.log.add("Monster already moved this " + \
                "turn.\n\n")
            return
        
        # 4. check destination tile occupancy
        if not tile_f.available_to_move():
            self.log.add("Destination already occupied.\n\n")
            return

        # 5. check valid path

        # 6. check enough movement crests

        # 7. everything is ok so move the monster
        tile_f.content = monster
        tile_i.remove_content()
        monster.move_cooldown = True
        self.set_start_message()

    #def run_attack_command(self, command):
    #    """
    #    Run command that makes a player monster attack.
    #    """
    # 1. get tiles
    # 2. get monster/target
    # 3. check cooldown
    # 4. check range
    # 5. check crest
    # 6. if target is monster and opponent has defense crest:
    #    call for defense state
    # 7. else simply produce the defense
        
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
            self.log.add("Origin out of bound.\n\n")
            return None, None
        if not self.duel.dungeon.in_bound(pos_f):
            self.log.add("Destination out of bound.\n\n")
            return None, None

        # check tiles are dungeon tiles
        tile_i = self.duel.dungeon.get_tile(pos_i)
        if not tile_i.is_dungeon():
            self.log.add("Origin is no dungeon path.\n\n")
            return None, None
        tile_f = self.duel.dungeon.get_tile(pos_f)
        if not tile_f.is_dungeon():
            self.log.add("Destination is no dungeon " + \
                "path.\n\n")
            return None, None

        return tile_i, tile_f

    def get_player_monster(self, tile):
        """
        Get monster at tile and check that it correspond to
        the current player.
        """
        # check if there is a monster at origin
        if not tile.has_monster():
            self.log.add("No monster at specified " + \
                "position.\n\n")
            return None

        # check if monster is player monster
        monster = tile.content
        if monster not in self.duel.player.monster_list.list:
            self.log.add("No player's monster.\n\n")
            return None

        return tile.content

def is_move_command(command):
    """
    Check if command is a move command. NOTE: it does not 
    check if the pos strings are valid or in bound.
    """
    len_ok    = command.len == 3
    param0_ok = command.equals_param(0, "m")
    param1_ok = not command.is_int(1)
    param2_ok = not command.is_int(2)

    return len_ok and param0_ok and param1_ok and param2_ok

def is_attack_command(command):
    """
    Check if a command is an attack command, either and 
    attack to an opponent monster or to the dungeon master.
    """
    correct_len = 1 <= command.len <= 2
    return correct_len and command.are_params_int()

help_text = "\n\n\
Dungeon commands: \n\
    m xy1 xy2: move monster at xy1 to position xy2\n\
    a xy1 xy2: use monster at xy1 to attack monster at xy2\n\
    f        : finish phase."
