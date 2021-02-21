class Summon():
    """
    Generic summon that is played in the board of the game.
    """
    def __init__(self, card, log):
        # attributes extracted from card
        self.name = card.name
        self.level = card.level
        self.chars = card.chars
        self.card = card
        self.log = log

    def is_monster(self):
        """
        Default is method.
        """
        return False

    def is_item(self):
        """
        Default is method.
        """
        return False
    
    def stringify(self):
        """
        Returns a string version of object.
        """
        return self.card.stringify()

    def stringify_short(self):
        """
        Returns one-liner string version of object.
        """
        return self.card.stringify_short()
