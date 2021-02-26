class Pos():
    """
    Defines a position in the y-x plane.
    """
    def __init__(self, y, x):
        self.y = y
        self.x = x

    @classmethod
    def from_string(cls, string):
        """
        Create a Pos object from string using alphabetical
        coordinates for the x position and numerical 
        coordinates for the y position (in that order). If
        the string is invalid, return None.
        """
        # test for string correct length
        if not (2 <= len(string) <= 3):
            return None

        x_string = string[0]
        y_string = string[1:]

        # test for valid y string
        try:
            y = int(y_string)
            y -= 1 # correct for user 1-indexing
        except ValueError:
            return None

        # get x value (no need to validate)
        x = ord(x_string) - 97

        return cls(y, x)

    # isometric transformation functions
    def turn_cw(self):
        """
        Turn position clock-wise 90 degrees.
        """
        temp_y = self.y
        self.y = -1*self.x
        self.x = temp_y

    def turn_ccw(self):
        """
        Turn position counter clock-wise 90 degrees.
        """
        temp_y = self.y
        self.y = self.x
        self.x = -1*temp_y

    def flip_lr(self):
        """
        Flip position left-right, that is, in the horizontal
        direction.
        """
        self.x = -1*self.x

    def flip_ud(self):
        """
        Flip position up-down, that is, in the vertical
        direction.
        """
        self.y = -1*self.y

    def stringify(self):
        """
        Returns string version of object.
        """
        # correct for python 0-indexing----v
        return chr(self.x+97) + str(self.y+1)

    # redefinition of built-in operations
    def __add__(self, other):
        """
        Redefinition of addition
        """
        return Pos(self.y + other.y, self.x + other.x)

    def __eq__(self, other):
        """
        Redefinition of equality.
        """
        if isinstance(other, self.__class__):
            return self.y == other.y and self.x == other.x
        else:
            return False
