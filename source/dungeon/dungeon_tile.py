from tile import Tile

class DungeonTile(Tile):
    """
    A dungeon tile where monsters can exist and move.
    """
    def __init__(self, char, content=None):
        self.char = char
        self.content = content # what it is over the tile

    def is_dungeon(self):
        return True

    def stringify(self):
        """
        Returns a string version of object.
        """
        # if tile has something, return the tile version of 
        # it
        if self.content is not None:
            return self.content.stringify_tile()
        else:
            return super().stringify()
