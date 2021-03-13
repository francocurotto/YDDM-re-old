from char_functions import select_chars

class Tile():
    """
    Generic dungeon tile.
    """
    def __init__(self):
        self.visited = False # used only for path calculation
        self.char = select_chars(self.char_ascii, 
            self.char_unicode, self.char_emoji)

    def is_dungeon(self):
        return False

    def stringify(self):
        """
        Returns a string version of object.
        """
        return "Can't print, nothing here."

    def stringify_short(self):
        """
        Returns a short string version of object.
        """
        return self.stringify()

    def stringify_tile(self):
        """
        Returns a tile string version of object.
        """
        return self.char
