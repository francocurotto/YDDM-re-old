from empty_tile import EmptyTile
from dice_nets.pos import Pos
from dungeon_object import DungeonObject

class Dungeon():
    """
    The board where the dice are dimensioned and the monsters
    interact.
    """
    # display icons
    chars_ascii   = {"block" : "[]"}
    chars_unicode = {"block" : "[]"}
    chars_emoji   = {"block" : "🔲"}

    # dungeon fixed values
    WIDTH  = 19
    HEIGHT = 13

    def __init__(self, players, log):
        self.log = log
        self.array  = []
        self.fill_array()
        self.chars = self.select_chars()

        # create initial tiles with monsterlord for each 
        # player. Player 1:
        player1 = players[0]
        tile = player1.create_tile(player1.monster_lord)
        self.set_tile(tile, Pos(6,0))
        # Player 2
        player2 = players[1]
        tile = player2.create_tile(player2.monster_lord)
        self.set_tile(tile, Pos(6,18))
        
    def fill_array(self):
        """
        Fill dungeon array with empty tiles
        """
        for _ in range(self.HEIGHT):
            row = []
            for _ in range(self.WIDTH):
                row.append(EmptyTile())
            self.array.append(row)

    def set_net(self, net, pos, player, summon):
        """
        Place net from player at position pos into dungeon.
        First check that the net can be properly placed in
        position. Return false if net cannot be placed.
        """
        # update net with position
        net.offset(pos)

        # check if net can be placed
        success = self.check_net(net, player)
        if not success:
            return success

        # if net can be placed, place it
        for pos in net.pos_list:
            if pos == net.center_pos: # center => add summon
                tile = player.create_tile(summon)
            else: # if not center pos, create empty tile
                tile = player.create_tile(DungeonObject())

            self.set_tile(tile, pos)

        return success

    def check_net(self, net, player):
        """
        Check if net can be properly placed in dungeon by
        player.
        """
        # check in bound condition
        for pos in net.pos_list:
            if not self.in_bound(pos):
                self.log.add("Dice net out of bound.\n")
                return False

        # check no overlaping condition
        for pos in net.pos_list:
            if self.overlaps(pos):
                self.log.add("Dice net overlaps dungeon " + \
                    "path\n")
                return False

        # check connection with player dungeon condition
        for pos in net.pos_list:
            neighbors = self.get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in player.tiles:
                    # last condition so I can safely return
                    # and escape of the nested loop. What
                    # happened to the good old days of GOTO?
                    return True

        self.log.add("Dice net does not connect with " + \
            "dungeon path\n")
        return False

    def in_bound(self, pos):
        """
        Check if a position, falls inside the dungeon array.
        """
        in_bound_y = 0 <= pos.y < len(self.array)
        in_bound_x = 0 <= pos.x < len(self.array[0])

        return in_bound_y and in_bound_x

    def overlaps(self, pos):
        """
        Checks if position overlaps with a dungeon tile 
        already existing in the dungeon.
        """
        tile = self.get_tile(pos)
        return tile.is_dungeon()

    def get_tile(self, pos):
        """
        Get tile at position pos (y,x).
        """
        # check pos is in bound
        if not self.in_bound(pos):
            return None

        return self.array[pos.y][pos.x]

    def set_tile(self, tile, pos):
        """
        Set tile at position pos (y,x), replacing previous 
        tile.
        """
        self.array[pos.y][pos.x] = tile

    def get_neighbors(self, pos):
        """
        get the neighbors tiles from tile at position pos.
        Neighbors are considered tiles that are horizontal
        and vertical adjacent only.
        """
        neighbor_pos_list = pos.get_neighbors()
        neighbor_tiles = []
        for neighbor_pos in neighbor_pos_list:
            if self.in_bound(neighbor_pos):
                neighbor_tile = self.get_tile(neighbor_pos)
                neighbor_tiles.append(neighbor_tile)

        return neighbor_tiles

    def get_path(self, pos_i, pos_f):
        """
        Return a path along the dungeon from pos_i to pos_f,
        considering the rules of DDM. The returned path is a 
        list of positions from start to finish. If no path is 
        found, return None.
        """
        #TODO: path search algorithm
        return [pos_i, pos_f]

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
            
            # create list of row strings
            tile_list = [t.stringify_tile() for t in row]
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
