from color_functions import color_fg, color_bg, grayout
from char_functions import select_chars
from target import Target

class MonsterLord(Target):
    """
    The representation of the player in the dungeon. When
    the monster lord is beaten the game is over.
    """
    heart_emoji = {"blue" : "💙",
                   "red"  : "❤️ "}
    def __init__(self, color):
        self.color = color
        self.hearts = 3
        
        # display characters
        self.chars_ascii = {
            "type"    : "ML",
            "heart"   : color_fg("<3", self.color),
            "noheart" : grayout("<3"),
            "tile"    : color_fg("ML", self.color)}
        self.chars_unicode = {
            "type"    : "♛",
            "heart"   : color_fg("♥", self.color),
            "noheart" : "♡",
            "tile"    : color_fg("♛♥", self.color)}
        self.chars_emoji = {
            "type"    : "👑",
            "heart"   : self.heart_emoji[self.color],
            "noheart" : "🖤",
            "tile"    : color_bg("👑", self.color)}

        self.chars = select_chars(self.chars_ascii, 
            self.chars_unicode, self.chars_emoji)

    def is_dead(self):
        """
        Check if monster lord has been beaten.
        """
        return self.hearts <= 0

    def is_monster_lord(self):
        """
        Necesary for checks in dungeon.
        """
        return True

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

    def stringify_short(self):
        """
        Returns a short string version of object.
        """
        return self.stringify()
