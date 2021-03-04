from tile import Tile

class DungeonTile(Tile):
    """
    A dungeon tile where monsters can exist and move.
    """
    def __init__(self, char, content=None):
        self.char = char
        self.content = content # what it is over the tile

    def remove_content(self):
        """
        Remove the current content (replaced by None), and
        return it.
        """
        content = self.content
        self.content = None
        return content

    def is_dungeon(self):
        return True

    def has_monster(self):
        """
        Returns True if tile contains a monster.
        """
        # first check if it is empty
        if self.content is None:
            return False

        return self.content.is_monster()

    def has_target(self):
        """
        Returns True if tile has valid target (monster or
        monster lord).
        """
        if self.content is None:
            return False

        is_monster = self.content.is_monster()
        is_ml = self.content.is_monster_lord()
        return is_monster or is_ml

    def available_to_move(self):
        """
        Returns True if a monster can move to tile.
        """
        return self.content is None or self.content.is_item()

    def stringify(self):
        """
        Returns a string version of content. If no content,
        returns message.
        """
        if self.content is not None:
            return self.content.stringify()
        else:
            return super().stringify()

    def stringify_short(self):
        """
        Returns a short string version of content. If no
        content, returns message.
        """
        if self.content is not None:
            return self.content.stringify_short()
        else:
            return super().stringify()

    def stringify_tile(self):
        """
        Returns a tile string version of object.
        """
        # if tile has something, return the tile version of 
        # it
        if self.content is not None:
            return self.content.stringify_tile()
        else:
            return super().stringify_tile()
