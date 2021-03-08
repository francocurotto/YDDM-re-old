from monster import Monster

class Warrior(Monster):
    """
    A monster of type warrior.
    """
    def __init__(self, card, color, log):
        super().__init__(card, color, log)

    def has_advantage_over_dragon(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_warrior()
