class Monster(Summon):
    """
    A monster in the board.
    """
    def __init__(self, card):
        # attributes extracted from card
        super().__init__(card)
        self.attack = self.card.attack
        self.defense = self.card.defense
        self.life = self.card.life
        self.ability = self.card.ability

    def stringify_short(self):
        """
        Returns a one-liner string version of object.
        """
        TODO
