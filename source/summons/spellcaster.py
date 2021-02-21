from monster import Monster

class Spellcaster(Monster):
    """
    A monster of type spellcaster.
    """
    def __init__(self, card, log):
        super().__init__(card, log)

    def has_advantage_over_undead(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_spellcaster()
