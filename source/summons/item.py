from summon import Summon

class Item(Summon):
    """
    An item in the board.
    """
    def __init__(self, card, log):
        # attributes extracted from card
        super().__init__(card, log)
        self.ability = self.card.ability

    def is_item(self):
        return True
