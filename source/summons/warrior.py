from monster import Monster

class Warrior(Monster):
    """
    A monster of type warrior.
    """
    def __init__(self, card, log):
        super().__init__(card, log)

    def has_advantage_over_dragon(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_warrior()
