hypercube = {
    "x1": 1,
    "y1": 1,
    "z1": 1,
    "w1": 1,

    "x2": 1,
    "y2": -1,
    "z2": 1,
    "w2": 1,

    "x3": -1,
    "y3": 1,
    "z3": 1,
    "w3": 1,

    "x4": -1,
    "y4": -1,
    "z4": 1,
    "w4": 1,

    "x5": 1,
    "y5": 1,
    "z5": -1,
    "w5": 1,

    "x6": 1,
    "y6": -1,
    "z6": -1,
    "w6": 1,

    "x7": -1,
    "y7": 1,
    "z7": -1,
    "w7": 1,

    "x8": -1,
    "y8": -1,
    "z8": -1,
    "w8": 1
}
#,
#    "x9 : 
#,   "y9 : 
#,   "z9 : 
#,   "w9 : 
#,
#    "x10 : 
#,   "y10 : 
#,   "z10 : 
#,   "w10 : 
#,
#    "x11 : 
#,   "y11 : 
#,   "z11 : 
#,   "w11 : 
#,
#    "x12 : 
#,   "y12 : 
#,   "z12 : 
#,   "w12 : 
#,
#    "x13 : 
#,   "y13 : 
#,   "z13 : 
#,   "w13 : 
#,
#    "x14 : 
#,   "y14 : 
#,   "z14 : 
#,   "w14 : 
#,
#    "x15 : 
#,   "y15 : 
#,   "z15 : 
#,   "w15 : 
#,
#    "x16 : 
#,   "y16 : 
#,   "z16 : 
#,   "w16 :
print("List of 4d points:", hypercube,"\n")
# converting 4d to 3d is the same as converting
# 3d to 2d, only one dimension louder.
# The simplest 3d to 2d case is using orthogonal
# projection and just ignoring z, you can do the
# same with 4d to 3d, just drop the last coord.
# Perspective transforms are the same, reduce the
# first three dimensions proportional to 1 / the
# fourth.
def _vertex1_():
    i = 1/int(hypercube["w1"])
    p1 = hypercube["x1"]/i
    p2 = hypercube["y1"]/i
    p3 = hypercube["z1"]/i
    _vertex1_.pts = [p1,p2,p3]
def _vertex2_():
    i = 1/int(hypercube["w2"])
    p1 = hypercube["x2"]/i
    p2 = hypercube["y2"]/i
    p3 = hypercube["z2"]/i
    _vertex2_.pts = [p1,p2,p3]
def _vertex3_():
    i = 1/int(hypercube["w3"])
    p1 = hypercube["x3"]/i
    p2 = hypercube["y3"]/i
    p3 = hypercube["z3"]/i
    _vertex3_.pts = [p1,p2,p3]
def _vertex4_():
    i = 1/int(hypercube["w4"])
    p1 = hypercube["x4"]/i
    p2 = hypercube["y4"]/i
    p3 = hypercube["z4"]/i
    _vertex4_.pts = [p1,p2,p3]
def _vertex5_():
    i = 1/int(hypercube["w5"])
    p1 = hypercube["x5"]/i
    p2 = hypercube["y5"]/i
    p3 = hypercube["z5"]/i
    _vertex5_.pts = [p1,p2,p3]
def _vertex6_():
    i = 1/int(hypercube["w6"])
    p1 = hypercube["x6"]/i
    p2 = hypercube["y6"]/i
    p3 = hypercube["z6"]/i
    _vertex6_.pts = [p1,p2,p3]
def _vertex7_():
    i = 1/int(hypercube["w7"])
    p1 = hypercube["x7"]/i
    p2 = hypercube["y7"]/i
    p3 = hypercube["z7"]/i
    _vertex7_.pts = [p1,p2,p3]
def _vertex8_():
    i = 1/int(hypercube["w8"])
    p1 = hypercube["x8"]/i
    p2 = hypercube["y8"]/i
    p3 = hypercube["z8"]/i
    _vertex8_.pts = [p1,p2,p3]
_vertex1_()
_vertex2_()
_vertex3_()
_vertex4_()
_vertex5_()
_vertex6_()
_vertex7_()
_vertex8_()
def _3d_():
    print("3D point 1",_vertex1_.pts,"\n","3D point 2",_vertex2_.pts,"\n","3D point 3",_vertex3_.pts,"\n","3D point 4",_vertex4_.pts,"\n","3D point 5",_vertex5_.pts,"\n","3D point 6",_vertex6_.pts,"\n","3D point 7",_vertex7_.pts,"\n","3D point 8",_vertex8_.pts)
_3d_()