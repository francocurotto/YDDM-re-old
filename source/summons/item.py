from summon import Summon

class Item(Summon):
    """
    An item in the board.
    """
    def __init__(self, card):
        # attributes extracted from card
        super().__init__(self, card)
        self.ability = self.card.ability
