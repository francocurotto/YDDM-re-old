from monster import Monster

class Spellcaster(Monster):
    """
    A monster of type spellcaster.
    """
    def __init__(self, card):
        super().__init__(card)
