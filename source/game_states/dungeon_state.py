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
        self.pos_i  = None
        self.tile_i = None
        self.pos_f  = None
        self.tile_f = None
        self.help_text = self.help_text + help_text

    def restart_new(self):
        """
        Restart state comming from new turn.
        """
        self.restart()

        # add title to start message
        state_title = "<DUNGEON PHASE> [f: finish]\n\n"
        self.start_message = state_title + self.start_message

    def restart(self):
        """
        Restart state.
        """
        # reset next state
        self.next_state = self

        # set start message
        self.start_message  = self.duel.dungeon.stringify()
        self.start_message += "\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # finish dungeon phase command
        if command.equals("f"):
            # decooldown monster
            self.duel.player.decooldown_monsters()

            # finish turn
            self.duel.advance_turn()
            self.next_state = self.roll_state
            self.next_state.restart()

        # move command
        elif is_move_command(command): 
            subcommand = command.subcommand(1)
            self.run_move_command(subcommand)

        # attack command
        elif is_attack_command(command):
            subcommand = command.subcommand(1)
            self.run_attack_command(subcommand)
        
        # generic commands
        else:
            super().update(command)

    def run_move_command(self, command):
        """
        Run command that makes a player monster to move in
        the dungeon.
        """
        # 1. get tiles
        success = self.get_pos_and_tiles(command)
        if not success:
            return

        # 2. get monster
        monster = self.get_player_monster(self.tile_i)
        if not monster:
            return

        # 3. check that monster hasn't move yet
        if monster.move_cooldown:
            self.log.add("Monster already moved this " + \
                "turn.\n\n")
            return
        
        # 4. check destination tile occupancy
        if self.tile_f.content.is_target():
            self.log.add("Destination already occupied.\n\n")
            return

        # 5. check valid path
        path = self.duel.dungeon.get_path(self.pos_i, 
            self.pos_f)
        if not path:
            self.log.add("Invalid movement path.\n\n")

        # 6. check enough movement crests
        move_cost = len(path) - 1
        if self.duel.player.crest_pool.movement < move_cost:
            self.log.add("Not enough movement crests.\n\n")
            return

        # 7. everything is ok so move the monster
        self.duel.player.crest_pool.movement -= move_cost
        self.tile_f.content = monster
        self.tile_i.remove_content()
        monster.move_cooldown = True
        self.restart()

    def run_attack_command(self, command):
        """
        Run command that makes a player monster attack.
        """
        # 1. get tiles
        success = self.get_pos_and_tiles(command)
        if not success:
            return

        # 2. get monster
        monster = self.get_player_monster(self.tile_i)
        if not monster:
            return

        # 3. get target
        target = self.get_opponent_target(self.tile_f)
        if not target:
            return

        # 4. check that monster hasn't attacked yet
        if monster.attack_cooldown:
            self.log.add("Monster already attacked this " + \
                "turn.\n\n")
            return

        # 5. check range
        if self.pos_i.distance_to(self.pos_f) > 1:
            self.log.add("Target out of range.\n\n")
            return

        # 6. check crest pool
        if self.duel.player.crest_pool.attack == 0:
            self.log.add("Not enough attack crests.\n\n")
            return

        # 7. attack is valid, first reduce attack crest
        self.duel.player.crest_pool.attack -= 1

        # 8.a. if target is monster
        if target.is_monster():
            self.log.add(monster.stringify_prebattle(target))
            # and if opponent can defend
            if self.duel.opponent.crest_pool.defense > 0:
                # trigger defense state
                self.next_state = self.def_state
                self.next_state.get_params(self)
                self.next_state.restart()
                return
            else: # simply attack monster
                self.log.add(self.duel.opponent.name + \
                    " has no defense crests.\n")
                monster.attack_monster(target, 
                    defending=False)
            # check for monsters death
            self.duel.player.check_for_death(self.tile_i)
            self.duel.opponent.check_for_death(self.tile_f)
        # 8.b. if target is monster lord
        else:
            monster.attack_ml(self.duel.opponent)

        self.log.add("\n")
        self.next_state.restart()

    def get_pos_and_tiles(self, command):
        """
        Get initial and final tiles, and it respective pos 
        from command. Return true if all the objects could be
        obtained. Used in move and attack commands.
        """
        pos_i = Pos.from_string(command.list[0])
        pos_f = Pos.from_string(command.list[1])

        # check valid positions
        if not pos_i or not pos_f:
            return False

        # check positions in bound
        if not self.duel.dungeon.in_bound(pos_i):
            self.log.add("Origin out of bound.\n\n")
            return False
        if not self.duel.dungeon.in_bound(pos_f):
            self.log.add("Destination out of bound.\n\n")
            return False

        # check tiles are dungeon tiles
        tile_i = self.duel.dungeon.get_tile(pos_i)
        if not tile_i.is_dungeon():
            self.log.add("Origin is no dungeon path.\n\n")
            return False
        tile_f = self.duel.dungeon.get_tile(pos_f)
        if not tile_f.is_dungeon():
            self.log.add("Destination is no dungeon " + \
                "path.\n\n")
            return False

        # if everyting went good, add pos and tiles to state
        # paramenters and return True
        self.pos_i  = pos_i
        self.tile_i = tile_i
        self.pos_f  = pos_f
        self.tile_f = tile_f
        return True

    def get_player_monster(self, tile):
        """
        Get monster at tile and check that it corresponds to
        the current player.
        """
        # check if there is a monster at tile
        if not tile.content.is_monster():
            self.log.add("No monster at specified " + \
                "position.\n\n")
            return None

        # check if monster is player monster
        monster = tile.content
        if monster not in self.duel.player.monster_list.list:
            self.log.add("Can't move opponent's " + \
                "monster.\n\n")
            return None

        return tile.content

    def get_opponent_target(self, tile):
        """
        Get opponent target from attack at tile and check 
        that it corresponds to a valid target.
        """
        # check if there is a target at tile
        if not tile.content.is_target():
            self.log.add("No target at specified " + \
                "position.\n\n")
            return None

        # check if target is opponent monster lord or 
        # opponent monster
        target = tile.content
        if not self.duel.opponent.owns_target(target):
            self.log.add("Can't attack own.\n\n")
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
    Check if a command is an attack command. NOTE: it does 
    not check if the pos strings are valid or in bound.
    """
    len_ok    = command.len == 3
    param0_ok = command.equals_param(0, "a")
    param1_ok = not command.is_int(1)
    param2_ok = not command.is_int(2)

    return len_ok and param0_ok and param1_ok and param2_ok

help_text = "\n\n\
Dungeon commands: \n\
    m xy1 xy2: move monster at xy1 to position xy2\n\
    a xy1 xy2: use monster at xy1 to attack target at xy2\n\
    f        : finish phase."
