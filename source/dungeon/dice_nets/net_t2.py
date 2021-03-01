from .dice_net import DiceNet
from .pos import Pos

class NetT2(DiceNet):
    """
    Dice net with a specific shape.
    """
    name = "T2"
    def __init__(self, log):
        super().__init__(log)
        self.pos_list = [Pos(-1,-1),Pos(-1,0),
                                    Pos(0,0),Pos(0,1),
                                    Pos(1,0),
                                    Pos(2,0)]
        self.center_pos = self.get_center_pos()
