import os, yaml
from settings import library_path
from dice_pool import DicePool
from player import Player
from dungeon import Dungeon

class Duel():
    """
    A duel were player are playing YDDM.
    """
    def __init__(self, pfile1, pfile2, log):
        self.log = log

        # For now, creates players with random pools
        self.players = self.create_players(pfile1, pfile2)
        self.player1 = self.players[0]
        self.player2 = self.players[1]

        # create dungeon
        self.dungeon = Dungeon(self.players, self.log)

        # define current player and opponent
        self.player = self.players[0]
        self.opponent = self.players[1]
        self.turn = 1

    def advance_turn(self):
        """
        Update the duel as if a turn has finished.
        """
        self.turn += 1
        
        temp = self.opponent # lame temp variable for swap
        self.opponent = self.player
        self.player = temp

    def finished(self):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfeit condition.
        """
        for player in self.players:
            # Forfeit condition
            if player.forfeited:
                self.log.add(player.name + " forfeited.\n")
                return True

            # normal win condition (monster lord beaten)
            if player.monster_lord.is_dead():
                opponent = self.get_opponent(player)
                self.log.add(opponent.name + 
                    " is the winner!\n" +
                    "Destroyed all opponent's hearts.\n")
                return True

        return False

    def check_for_casualties(self, attacker, attacked):
        """
        Check if any of the players has a monster that has
        died after an attack. If one monster is death,
        remove from dungeon.
        """
        self.player.check_for_death(attacker)
        self.opponent.check_for_death(attacked)

    def get_opponent(self, player):
        """
        Get opponent of player.
        """
        return (set(self.players) - set([player])).pop()

    def create_players(self, pfile1, pfile2):
        """
        Helper function to initialize a duel with two players 
        with the given pools (or random pools).
        """
        # generate players pools
        pool1 = self.create_pool(pfile1)
        pool2 = self.create_pool(pfile2)
    
        # generate players
        player1 = Player("Player 1", "blue", pool1, self.log)
        player2 = Player("Player 2", "red",  pool2, self.log)
    
        return [player1, player2]   

    def create_pool(self, pool_file):
        """
        Create a dice pool given the information of the dice 
        file and library. If not dice file, create random 
        pool.
        """
        # create dice pool
        dice_pool = DicePool(self.log)

        # check if pool file argument was given
        if not pool_file:
            dice_pool.fill_random()
            return dice_pool
        
        # check if pool file exists
        if not os.path.isfile(pool_file):
            self.log.add("File " + pool_file + " not " +
            "found.\nUsing random dice pool instead.\n")
            dice_pool.fill_random()
            return dice_pool

        # try to get yaml data from file
        id_list = yaml.full_load(open(pool_file))

        # fill dice pool
        dice_pool.fill_from_ids(id_list)

        return dice_pool
