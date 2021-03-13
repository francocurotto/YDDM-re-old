from color_functions import color_fg
from tile import Tile
from dungeon_object import DungeonObject

class DungeonTile(Tile):
    """
    A dungeon tile where monsters can exist and move.
    """
    def __init__(self, color, content):
        self.char_ascii   = color_fg("[]", color)
        self.char_unicode = color_fg("[]", color)
        if color == "blue":
            self.char_emoji = "🟦" 
        elif color == "red":
            self.char_emoji = "🟥" 

        self.content = content # what it is over the tile
        super().__init__()

    def remove_content(self):
        """
        Remove the current content (replaced by None), and
        return it.
        """
        self.content = DungeonObject()

    def is_dungeon(self):
        return True

    def stringify(self):
        """
        Returns a string version of content.
        """
        return self.content.stringify()

    def stringify_short(self):
        """
        Returns a short string version of content.
        """
        return self.content.stringify_short()

    def stringify_tile(self):
        """
        Returns a tile string version of object.
        """
        # if tile has something, return the tile version of 
        # it
        if self.content.is_printable():
            return self.content.stringify_tile()
        else:
            return super().stringify_tile()
