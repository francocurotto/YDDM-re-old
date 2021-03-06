from summon import Summon

class Item(Summon):
    """
    An item in the board.
    """
    def __init__(self, card, chars, log):
        super().__init__(card, chars, log)
        self.tile_char = chars["item"]

    def add_to_player_list(self, player):
        """
        Add item to the proper player list when summoning.
        """
        player.item_list.add(self)

    def is_item(self):
        return True
