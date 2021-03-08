from monster import Monster

class Spellcaster(Monster):
    """
    A monster of type spellcaster.
    """
    def __init__(self, card, color, log):
        super().__init__(card, color, log)

    def has_advantage_over_undead(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_spellcaster()
