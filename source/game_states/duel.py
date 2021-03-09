from player import Player
from dice_list import DiceLibrary
from dungeon import Dungeon

class Duel():
    """
    A duel were player are playing YDDM.
    """
    def __init__(self, log):
        self.log = log

        # For now, creates players with random pools
        self.player1, self.player2 = self.random_init()
        self.players = [self.player1, self.player2]

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

    def random_init(self):
        """
        Helper function to initialize a duel with two players 
        with random dice pools.
        """
        # generate dice library
        from settings import library_path
        library = DiceLibrary(self.log)
        library.fill_from_file(library_path)
    
        # generate players
        player1 = Player("Player 1", "blue", self.log)
        player2 = Player("Player 2", "red", self.log)
    
        # fill dice pool of players with random dice
        player1.dice_pool.fill_random(library)
        player2.dice_pool.fill_random(library)
            
        return player1, player2   
