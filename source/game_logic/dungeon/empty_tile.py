from color_functions import grayout
from tile import Tile

class EmptyTile(Tile):
    """
    Tile with no dungeon path in it.
    """
    # display icons
    char_ascii   = grayout("[]")
    char_unicode = grayout("[]")
    char_emoji   = "⬛" 

    def __init__(self):
        super().__init__()
