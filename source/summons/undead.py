from monster import Monster

class Undead(Monster):
    """
    A monster of type undead.
    """
    def __init__(self, card, log):
        super().__init__(card, log)

    def has_advantage_over_beast(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_undead()
