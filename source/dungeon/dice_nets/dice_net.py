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

def create_net(string, log):
    #imports
    from .net_t1 import NetT1
    from .net_t2 import NetT2
    from .net_z1 import NetZ1
    from .net_z2 import NetZ2
    from .net_x1 import NetX1
    from .net_x2 import NetX2
    from .net_m1 import NetM1
    from .net_m2 import NetM2
    from .net_s1 import NetS1
    from .net_s2 import NetS2
    from .net_l1 import NetL1

    # conditional returns
    if string == "T1":
        return NetT1(log)
    if string == "T2":
        return NetT2(log)
    if string == "Z1":
        return NetZ1(log)
    if string == "Z2":
        return NetZ2(log)
    if string == "X1":
        return NetX1(log)
    if string == "X2":
        return NetX2(log)
    if string == "M1":
        return NetM1(log)
    if string == "M2":
        return NetM2(log)
    if string == "S1":
        return NetS1(log)
    if string == "S2":
        return NetS2(log)
    if string == "L1":
        return NetL1(log)
    # invalid net name
    return None
