class DiceNet():
    """
    Positions of the tiles created when a dice is dimensioned
    (unfolded).
    """
    def apply_trans(self, trans_list):
        """
        Apply a list of transformations, identified by 
        strings to the net.
        """
        for trans in trans_list:
            # turn clock-wise
            if trans == "tcw":
                self.turn_cw()
            elif trans == "tccw":
                self.turn_ccw()
            elif trans == "flr":
                self.flip_lr()
            elif trans == "fud":
                self.flip_ud()

    def offset(self, offset):
        """
        Move all positions on net an offset amount. 
        """
        for pos in self.pos_list:
            pos = pos + offset
        
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
