from functions import grayout

class MonsterLord():
    """
    The representation of the player in the dungeon. When
    the monster lord is beaten the game is over.
    """
    def __init__(self, ml_chars):
        self.hearts = 3
        self.chars_ascii = {"type"    : "ML",
                            "noheart" : grayout("<3")}
        self.chars_unicode = {"type"    : "♛",
                              "noheart" : "♡"}
        self.chars_emoji = {"type"    : "👑",
                            "noheart" : "🖤"}

        self.chars = self.select_chars()
        # add player specific chars
        self.chars["heart"] = ml_chars["heart"]
        self.chars["tile"]  = ml_chars["tile"]

    def is_dead(self):
        """
        Check if monster lord has been beaten.
        """
        return self.hearts <= 0

    def is_monster(self):
        """
        Necesary for checks in dungeon.
        """
        return False

    def is_item(self):
        """
        Necesary for checks in dungeon.
        """
        return False

    def is_monster_lord(self):
        """
        Necesary for checks in dungeon.
        """
        return True

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing monster lord information.
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
        string = self.chars["type"] + " "
        
        # current hearts
        for _ in range(self.hearts):
            string += self.chars["heart"]

        # dead hearts
        for _ in range(3 - self.hearts):
            string += self.chars["noheart"]

        return string

    def stringify_tile(self):
        """
        Returns tile string version of object.
        """
        return self.chars["tile"]
