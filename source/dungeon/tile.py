class Tile():
    """
    Generic dungeon tile.
    """
    def __init__(self):
        self.char = self.select_char()

    def is_dungeon(self):
        return False

    def select_char(self):
        """
        Select the type of characters that will be used when
        printing the tile.
        """
        # weird import here so that the print_type parameter
        # can be changed at runtime
        from settings import print_type
        
        if print_type == "ascii":
            return self.char_ascii
        elif print_type == "unicode":
            return self.char_unicode
        elif print_type == "emoji":
            return self.char_emoji

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
