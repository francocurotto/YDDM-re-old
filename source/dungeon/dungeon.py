from empty_tile import EmptyTile

class Dungeon():
    """
    The board where the dice are dimensioned and the monsters
    interact.
    """
    # display icons
    chars_ascii   = {"block" : "[]"}
    chars_unicode = {"block" : "██"}
    chars_emoji   = {"block" : "🔲"}

    # dungeon fixed values
    WIDTH  = 19
    HEIGHT = 13

    def __init__(self):
        self.array  = []
        self.fill_array()
        self.chars = self.select_chars()
        
    def fill_array(self):
        """
        Fill dungeon array with empty tiles
        """
        for _ in range(self.HEIGHT):
            row = []
            for _ in range(self.WIDTH):
                row.append(EmptyTile())
            self.array.append(row)

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing the dungeon.
        """
        # weird import here so that the print_type parameter
        # can be changed at runtime
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
        # list of rows
        row_list = []

        # create first row (coordinates)
        row1 = self.create_coor_string("    ") # offset 4
        row_list.append(row1)

        # create second row blocks
        row2 = self.create_block_string()
        row_list.append(row2)

        # create rest of rows
        for i,row in enumerate(self.array):
            # string before row
            prefix = str(i+1).rjust(2) + self.chars["block"]
            
            # create los of row strings
            tile_list = [tile.stringify() for tile in row]
            tile_str  = "".join(tile_list)

            # string after row
            suffix = self.chars["block"] + str(i+1)

            # combine all
            row_str = prefix + tile_str + suffix
            row_list.append(row_str)

        # create bottom block row
        row16 = self.create_block_string()
        row_list.append(row16)

        # create last (coordinates)
        row17 = self.create_coor_string("     ") # offset 5
        row_list.append(row17)

        # join all rows
        string = "\n".join(row_list)

        return string

    def create_coor_string(self, offset):
        """
        Create a row of letter coordinates, starting with
        offset string.
        """
        letters = [chr(i) for i in range(97, 97+self.WIDTH)]
        return offset + " ".join(letters)
 
    def create_block_string(self):
        """
        Create a row of blocks.
        """
        return "  " + (self.WIDTH+2)*self.chars["block"]
