class DiceNet():
    """
    Positions of the tiles created when a dice is dimensioned
    (unfolded).
    """
    def __init__(self, log):
        self.log = log

    def apply_trans(self, trans_list):
        """
        Apply a list of transformations, identified by 
        strings to the net.
        """
        for trans in trans_list:
            if trans == "tcw": # turn clock-wise
                self.turn_cw()
            elif trans == "tccw": # turn counter clock-wise
                self.turn_ccw()
            elif trans == "flr": # flip left-right
                self.flip_lr()
            elif trans == "fud": # flip up-down
                self.flip_ud()
            else: # invalid transformation
                self.log.add("Invalid transformation\n")
                return False

        return True

    def offset(self, offset):
        """
        Move all positions on net an offset amount. 
        """
        new_pos = [pos + offset for pos in self.pos_list]
        self.pos_list = new_pos
        
    def turn_cw(self):
        """
        Turn all positions on net clock-wise 90 degrees.
        """
        for pos in self.pos_list:
            pos.turn_cw()

    def turn_ccw(self):
        """
        Turn all positions on net counter clock-wise 90
        degrees.
        """
        for pos in self.pos_list:
            pos.turn_ccw()

    def flip_lr(self):
        """
        Turn all positions on net left-right.
        """
        for pos in self.pos_list:
            pos.flip_lr()

    def flip_ud(self):
        """
        Turn all positions on net up-down.
        """
        for pos in self.pos_list:
            pos.flip_ud()
