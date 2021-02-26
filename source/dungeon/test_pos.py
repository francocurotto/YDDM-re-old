from pos import Pos

# test equality
assert(Pos(2,1) == Pos(2,1))
assert(Pos(1,1) != Pos(2,2))

# test addition
assert(Pos(3,5) == Pos(3,0)+Pos(0,5))
assert(Pos(0,0) == Pos(-9,7)+Pos(9,-7))

# test rotatios
p = Pos(3,1); p.turn_cw()
assert(p == Pos(-1,3))
p = Pos(-4,-5); p.turn_ccw()
assert(p == Pos(-5,4))

# test flips
p = Pos(2,-1); p.flip_lr()
assert(p == Pos(2,1))
p = Pos(2,-1); p.flip_ud()
assert(p == Pos(-2,-1))

# test string constructor
assert(Pos.from_string("sadf") is None) 
assert(Pos.from_string("c551") is None) 
assert(Pos.from_string("5c") is None) 
#
assert(Pos.from_string("a10") == Pos(9,0))
assert(Pos.from_string("c5") == Pos(4,2))

print("All test passed!")
