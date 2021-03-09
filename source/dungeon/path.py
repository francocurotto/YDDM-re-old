class Path():
    """
    A list of positions of the dungeon that represents a path
    through dungeon tiles.
    """
    def __init__(self, pos_list):
        self.list = pos_list

    def end(self):
        """
        Return the end position of the path.
        """
        return self.list[-1]

    def expand(self, dungeon):
        """
        Returns a list of paths that expand from the last
        position of the path, in all possible directions 
        according to the DDM rules. The rules include:
        - you can only expand through dungeon tiles.
        - you cannot expand through tiles occupied by 
            monsters or monster lords
        - you cand expand through a tile occupied by an item,
            but you can't expand further from that.
        """
        # get path end
        last_pos = self.end()

        # check if last tile has an item
        last_tile = dungeon.get_tile(last_pos)
        if last_tile.content.is_item():
            # if is item, you can't expand further
            return []

        # get the neighbors pos to expand
        neighbor_pos = last_pos.get_neighbors()

        new_paths = []
        # for each neighbor, check if they satisfy all the
        # requirements to expand the path
        for pos in neighbor_pos:
            # 1. must be in bound and a dungeon tile
            tile = dungeon.get_tile(pos)
            if tile is None or not tile.is_dungeon():
                continue

            # 2. must not be occupied by an obstacle (target)
            if tile.content.is_target():
                continue

            # 3. must not have been visited before
            if tile.visited:
                continue

            # all conditions met, add new path
            new_paths.append(Path(self.list + [pos]))
            tile.visited = True

        return new_paths

    def stringify(self):
        """
        Returns a string version of object.
        """
        str_list = [pos.stringify() for pos in self.list]
        string = "|".join(str_list)

        return string
