from empty_tile import EmptyTile

class Dungeon():
    """
    The board where the dice are dimensioned and the monsters
    interact.
    """
    def __init__(self):
        self.WIDTH  = 19
        self.HEIGHT = 13
        self.array  = []
        self.fill_array()

        # display icons
        self.chars_ascii   = {"block" : []}
        self.chars_unicode = {"block" : ██}
        self.chars_emoji   = {"block" : 🔲}

    def fill_array(self):
        """
        Fill dungeon array with empty tiles
        """
        for _ in self.WIDTH:
            col = []
            for _ in self.HEIGHT:
                col.append(EmptyTile())
            self.array.append(col)
