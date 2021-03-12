class DungeonObject():
    """
    An object in the dungeon.
    """
    # is functions default False
    def is_monster(self):
        return False

    def is_item(self):
        return False

    def is_monster_lord(self):
        return False

    def is_target(self):
        return False

    def is_printable(self):
        """
        Printable items are monsters, items and monster lord.
        """
        return self.is_target() or self.is_item()

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing object information.
        """
        from settings import print_type
        if print_type == "ascii":
            return self.chars_ascii
        elif print_type == "unicode":
            return self.chars_unicode
        elif print_type == "emoji":
            return self.chars_emoji

    def stringify(self):
        """
        Returns a string version of object.
        """
        return "Can't print, nothing here."

    def stringify_short(self):
        """
        Returns a string version of object.
        """
        return self.stringify()

    def stringify_tile(self):
        """
        Returns a tile string version of object.
        """
        return self.chars["tile"]
