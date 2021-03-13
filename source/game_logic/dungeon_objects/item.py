from color_functions import color_fg
from summon import Summon

class Item(Summon):
    """
    An item in the board.
    """
    def __init__(self, card, color, log):
        # display chars
        self.chars_ascii   = {"tile" : color_fg("IT", color)}
        self.chars_unicode = {"tile" : color_fg("??", color)}
        super().__init__(card, color, log)

    def add_to_player_list(self, player):
        """
        Add item to the proper player list when summoning.
        """
        player.item_list.add(self)

    def is_item(self):
        return True
