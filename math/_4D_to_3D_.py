#    Graphics-Driver: A graphics driver made by an idiot for an idiot.
#    Copyright (C) <2024>  <Ryan Britton Maxson, Phbar1945, Райан Махъссон>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
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
    "w8": 1,

    "x9": 1,
    "y9": 1,
    "z9": 1,
    "w9": -1,

    "x10": 1,
    "y10": -1,
    "z10": 1,
    "w10": -1,

    "x11": -1,
    "y11": 1,
    "z11": 1,
    "w11": -1,

    "x12": -1,
    "y12": -1,
    "z12": 1,
    "w12": -1,

    "x13": 1,
    "y13": 1,
    "z13": -1,
    "w13": -1,

    "x14": 1,
    "y14": -1,
    "z14": -1,
    "w14": -1,

    "x15": -1,
    "y15": 1,
    "z15": -1,
    "w15": -1,

    "x16": -1,
    "y16": -1,
    "z16": -1,
    "w16": -1
}
# Logger:
print("List of 4D points:", hypercube)
# converting 4d to 3d is the same as converting
# 3d to 2d, only one dimension louder.
# The simplest 3d to 2d case is using orthogonal
# projection and just ignoring z, you can do the
# same with 4d to 3d, just drop the last coord.
# Perspective transforms are the same, reduce the
# first three dimensions proportional to 1 / the      Vertex function:
# fourth.                                             First, don't create a var i of the 4D point, w. You
def _vertex1_():                                    # want to make stuff look more complicated than it is.
    x = float(hypercube["x1"])/float(hypercube["w1"]) if float(hypercube["w1"]) else float(hypercube["x1"])  # \
    y = float(hypercube["y1"])/float(hypercube["w1"]) if float(hypercube["w1"]) else float(hypercube["y1"])  #  } Divide x, y, and z by w if w != 0. if w = 0, return numerator.
    z = float(hypercube["z1"])/float(hypercube["w1"]) if float(hypercube["w1"]) else float(hypercube["z1"])  # /  Create a not-so-local-var of the new 3D point for later
    _vertex1_.pts = {"p1":x,"p2":y,"p3":z}                                                                  # use OUTSIDE of the function, or in other words,"Do what
def _vertex2_():                                                                                            # is not meant to be." Repeat 16 times.
    x = float(hypercube["x2"])/float(hypercube["w2"]) if float(hypercube["w2"]) else float(hypercube["x2"])
    y = float(hypercube["y2"])/float(hypercube["w2"]) if float(hypercube["w2"]) else float(hypercube["y2"])
    z = float(hypercube["z2"])/float(hypercube["w2"]) if float(hypercube["w2"]) else float(hypercube["z2"])
    _vertex2_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex3_():
    x = float(hypercube["x3"])/float(hypercube["w3"]) if float(hypercube["w3"]) else float(hypercube["x3"])
    y = float(hypercube["y3"])/float(hypercube["w3"]) if float(hypercube["w3"]) else float(hypercube["y3"])
    z = float(hypercube["z3"])/float(hypercube["w3"]) if float(hypercube["w3"]) else float(hypercube["z3"])
    _vertex3_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex4_():
    x = float(hypercube["x4"])/float(hypercube["w4"]) if float(hypercube["w4"]) else float(hypercube["x4"])
    y = float(hypercube["y4"])/float(hypercube["w4"]) if float(hypercube["w4"]) else float(hypercube["y4"])
    z = float(hypercube["z4"])/float(hypercube["w4"]) if float(hypercube["w4"]) else float(hypercube["z4"])
    _vertex4_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex5_():
    x = float(hypercube["x5"])/float(hypercube["w5"]) if float(hypercube["w5"]) else float(hypercube["x5"])
    y = float(hypercube["y5"])/float(hypercube["w5"]) if float(hypercube["w5"]) else float(hypercube["y5"])
    z = float(hypercube["z5"])/float(hypercube["w5"]) if float(hypercube["w5"]) else float(hypercube["z5"])
    _vertex5_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex6_():
    x = float(hypercube["x6"])/float(hypercube["w6"]) if float(hypercube["w6"]) else float(hypercube["x6"])
    y = float(hypercube["y6"])/float(hypercube["w6"]) if float(hypercube["w6"]) else float(hypercube["y6"])
    z = float(hypercube["z6"])/float(hypercube["w6"]) if float(hypercube["w6"]) else float(hypercube["z6"])
    _vertex6_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex7_():
    x = float(hypercube["x7"])/float(hypercube["w7"]) if float(hypercube["w7"]) else float(hypercube["x7"])
    y = float(hypercube["y7"])/float(hypercube["w7"]) if float(hypercube["w7"]) else float(hypercube["y7"])
    z = float(hypercube["z7"])/float(hypercube["w7"]) if float(hypercube["w7"]) else float(hypercube["z7"])
    _vertex7_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex8_():
    x = float(hypercube["x8"])/float(hypercube["w8"]) if float(hypercube["w8"]) else float(hypercube["x8"])
    y = float(hypercube["y8"])/float(hypercube["w8"]) if float(hypercube["w8"]) else float(hypercube["y8"])
    z = float(hypercube["z8"])/float(hypercube["w8"]) if float(hypercube["w8"]) else float(hypercube["z8"])
    _vertex8_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex9_():
    x = float(hypercube["x9"])/float(hypercube["w9"]) if float(hypercube["w9"]) else float(hypercube["x9"])
    y = float(hypercube["y9"])/float(hypercube["w9"]) if float(hypercube["w9"]) else float(hypercube["y9"])
    z = float(hypercube["z9"])/float(hypercube["w9"]) if float(hypercube["w9"]) else float(hypercube["z9"])
    _vertex9_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex10_():
    x = float(hypercube["x10"])/float(hypercube["w10"]) if float(hypercube["w10"]) else float(hypercube["x10"])
    y = float(hypercube["y10"])/float(hypercube["w10"]) if float(hypercube["w10"]) else float(hypercube["y10"])
    z = float(hypercube["z10"])/float(hypercube["w10"]) if float(hypercube["w10"]) else float(hypercube["z10"])
    _vertex10_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex11_():
    x = float(hypercube["x11"])/float(hypercube["w11"]) if float(hypercube["w11"]) else float(hypercube["x11"])
    y = float(hypercube["y11"])/float(hypercube["w11"]) if float(hypercube["w11"]) else float(hypercube["y11"])
    z = float(hypercube["z11"])/float(hypercube["w11"]) if float(hypercube["w11"]) else float(hypercube["z11"])
    _vertex11_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex12_():
    x = float(hypercube["x12"])/float(hypercube["w12"]) if float(hypercube["w12"]) else float(hypercube["x12"])
    y = float(hypercube["y12"])/float(hypercube["w12"]) if float(hypercube["w12"]) else float(hypercube["y12"])
    z = float(hypercube["z12"])/float(hypercube["w12"]) if float(hypercube["w12"]) else float(hypercube["z12"])
    _vertex12_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex13_():
    x = float(hypercube["x13"])/float(hypercube["w13"]) if float(hypercube["w13"]) else float(hypercube["x13"])
    y = float(hypercube["y13"])/float(hypercube["w13"]) if float(hypercube["w13"]) else float(hypercube["y13"])
    z = float(hypercube["z13"])/float(hypercube["w13"]) if float(hypercube["w13"]) else float(hypercube["z13"])
    _vertex13_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex14_():
    x = float(hypercube["x14"])/float(hypercube["w14"]) if float(hypercube["w14"]) else float(hypercube["x14"])
    y = float(hypercube["y14"])/float(hypercube["w14"]) if float(hypercube["w14"]) else float(hypercube["y14"])
    z = float(hypercube["z14"])/float(hypercube["w14"]) if float(hypercube["w14"]) else float(hypercube["z14"])
    _vertex14_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex15_():
    x = float(hypercube["x15"])/float(hypercube["w15"]) if float(hypercube["w15"]) else float(hypercube["x15"])
    y = float(hypercube["y15"])/float(hypercube["w15"]) if float(hypercube["w15"]) else float(hypercube["y15"])
    z = float(hypercube["z15"])/float(hypercube["w15"]) if float(hypercube["w15"]) else float(hypercube["z15"])
    _vertex15_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex16_():
    x = float(hypercube["x16"])/float(hypercube["w16"]) if float(hypercube["w16"]) else float(hypercube["x16"])
    y = float(hypercube["y16"])/float(hypercube["w16"]) if float(hypercube["w16"]) else float(hypercube["y16"])
    z = float(hypercube["z16"])/float(hypercube["w16"]) if float(hypercube["w16"]) else float(hypercube["z16"])
    _vertex16_.pts = {"p1":x,"p2":y,"p3":z}

_vertex1_() # Run each function to store local variable in memory.
_vertex2_()
_vertex3_()
_vertex4_()
_vertex5_()
_vertex6_()
_vertex7_()
_vertex8_()
_vertex9_()
_vertex10_()
_vertex11_()
_vertex12_()
_vertex13_()
_vertex14_()
_vertex15_()
_vertex16_()
# Logger:
print( "\n","3D point 1",_vertex1_.pts,"\n","3D point 2",_vertex2_.pts,"\n","3D point 3",_vertex3_.pts,"\n","3D point 4",_vertex4_.pts,
       "\n","3D point 5",_vertex5_.pts,"\n","3D point 6",_vertex6_.pts,"\n","3D point 7",_vertex7_.pts,"\n","3D point 8",_vertex8_.pts,
 "\n","3D point 9",_vertex9_.pts,"\n","3D point 10",_vertex10_.pts,"\n","3D point 11",_vertex11_.pts,"\n","3D point 12",_vertex12_.pts,
"\n","3D point 13",_vertex13_.pts,"\n","3D point 14",_vertex14_.pts,"\n","3D point 15",_vertex15_.pts,"\n","3D point 16",_vertex16_.pts
    )
def _3d_():         # 4 3D points per line to make it look complicated
    _3d_.dat1 = _vertex1_.pts # use a "pointer" to locate the float and access it from memory.
    _3d_.dat2 = _vertex2_.pts
    _3d_.dat3 = _vertex3_.pts
    _3d_.dat4 = _vertex4_.pts
    _3d_.dat5 = _vertex5_.pts
    _3d_.dat6 = _vertex6_.pts
    _3d_.dat7 = _vertex7_.pts
    _3d_.dat8 = _vertex8_.pts
    _3d_.dat9 = _vertex9_.pts
    _3d_.dat10 = _vertex10_.pts
    _3d_.dat11 = _vertex11_.pts
    _3d_.dat12 = _vertex12_.pts
    _3d_.dat13 = _vertex13_.pts
    _3d_.dat14 = _vertex14_.pts
    _3d_.dat15 = _vertex15_.pts
    _3d_.dat16 = _vertex16_.pts