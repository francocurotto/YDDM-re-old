from tile import Tile

class DungeonTile(Tile):
    """
    A dungeon tile where monsters can exist and move.
    """
    def __init__(self, chars):
        self.char_ascii   = chars["ascii"]
        self.char_unicode = chars["unicode"]
        self.char_emoji   = chars["emoji"]
        super().__init__()
