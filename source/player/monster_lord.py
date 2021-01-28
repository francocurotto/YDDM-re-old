class MonsterLord():
    """
    The representation of the player in the dungeon. When
    the monster lord is beaten the game is over.
    """
    def __init__(self):
        self.hearts = 3

    def is_dead(self):
        """
        Check if monster lord has been beaten.
        """
        return self.hearts <= 0
