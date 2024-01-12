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
    "w8": 1

#    "x9" : ,
#    "y9" : ,
#    "z9" : ,
#    "w9" : ,
#
#    "x10" : ,
#    "y10" : ,
#    "z10" : ,
#    "w10" : ,
#
#    "x11" : ,
#    "y11" : ,
#    "z11" : ,
#    "w11" : ,
#
#    "x12" : ,
#    "y12" : ,
#    "z12" : ,
#    "w12" : ,
#
#    "x13" : ,
#    "y13" : ,
#    "z13" : ,
#    "w13" : ,
#
#    "x14" : ,
#    "y14" : ,
#    "z14" : ,
#    "w14" : ,
#
#    "x15" : ,
#    "y15" : ,
#    "z15" : ,
#    "w15" : ,
#
#    "x16" : ,
#    "y16" : ,
#    "z16" : ,
#    "w16" : ,
}
print("List of 4D points:", hypercube)
# converting 4d to 3d is the same as converting
# 3d to 2d, only one dimension louder.
# The simplest 3d to 2d case is using orthogonal
# projection and just ignoring z, you can do the
# same with 4d to 3d, just drop the last coord.
# Perspective transforms are the same, reduce the
# first three dimensions proportional to 1 / the    # Vertex function:
# fourth.                                           # First, don't create a var i of the 4D point, w. You
def _vertex1_():                                    # want to make stuff look more complicated than it is.
    x = float(hypercube["x1"])/float(hypercube["w1"])  # \
    y = float(hypercube["y1"])/float(hypercube["w1"])  #  } Divide x, y, and z by w
    z = float(hypercube["z1"])/float(hypercube["w1"])  # /
    _vertex1_.pts = {"p1":x,"p2":y,"p3":z}          # Create a not-so-local-var of the new 3D point for later
def _vertex2_():                                    # use OUTSIDE of the function, or in other words,"Do what
    x = float(hypercube["x2"])/float(hypercube["w2"])  # is not meant to be." Repeat 16 times.
    y = float(hypercube["y2"])/float(hypercube["w2"])
    z = float(hypercube["z2"])/float(hypercube["w2"])
    _vertex2_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex3_():
    x = float(hypercube["x3"])/float(hypercube["w3"])
    y = float(hypercube["y3"])/float(hypercube["w3"])
    z = float(hypercube["z3"])/float(hypercube["w3"])
    _vertex3_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex4_():
    x = float(hypercube["x4"])/float(hypercube["w4"])
    y = float(hypercube["y4"])/float(hypercube["w4"])
    z = float(hypercube["z4"])/float(hypercube["w4"])
    _vertex4_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex5_():
    x = float(hypercube["x5"])/float(hypercube["w5"])
    y = float(hypercube["y5"])/float(hypercube["w5"])
    z = float(hypercube["z5"])/float(hypercube["w5"])
    _vertex5_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex6_():
    x = float(hypercube["x6"])/float(hypercube["w6"])
    y = float(hypercube["y6"])/float(hypercube["w6"])
    z = float(hypercube["z6"])/float(hypercube["w6"])
    _vertex6_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex7_():
    x = float(hypercube["x7"])/float(hypercube["w7"])
    y = float(hypercube["y7"])/float(hypercube["w7"])
    z = float(hypercube["z7"])/float(hypercube["w7"])
    _vertex7_.pts = {"p1":x,"p2":y,"p3":z}
def _vertex8_():
    x = float(hypercube["x8"])/float(hypercube["w8"])
    y = float(hypercube["y8"])/float(hypercube["w8"])
    z = float(hypercube["z8"])/float(hypercube["w8"])
    _vertex8_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex9_():
#    x = float(hypercube["x9"])/float(hypercube["w9"])
#    y = float(hypercube["y9"])/float(hypercube["w9"])
#    z = float(hypercube["z9"])/float(hypercube["w9"])
#    _vertex9_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex10_():
#    x = float(hypercube["x10"])/float(hypercube["w10"])
#    y = float(hypercube["y10"])/float(hypercube["w10"])
#    z = float(hypercube["z10"])/float(hypercube["w10"])
#    _vertex10_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex11_():
#    x = float(hypercube["x11"])/float(hypercube["w11"])
#    y = float(hypercube["y11"])/float(hypercube["w11"])
#    z = float(hypercube["z11"])/float(hypercube["w11"])
#    _vertex11_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex12_():
#    x = float(hypercube["x12"])/float(hypercube["w12"])
#    y = float(hypercube["y12"])/float(hypercube["w12"])
#    z = float(hypercube["z12"])/float(hypercube["w12"])
#    _vertex12_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex13_():
#    x = float(hypercube["x13"])/float(hypercube["w13"])
#    y = float(hypercube["y13"])/float(hypercube["w13"])
#    z = float(hypercube["z13"])/float(hypercube["w13"])
#    _vertex13_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex14_():
#    x = float(hypercube["x14"])/float(hypercube["w14"])
#    y = float(hypercube["y14"])/float(hypercube["w14"])
#    z = float(hypercube["z14"])/float(hypercube["w14"])
#    _vertex14_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex15_():
#    x = float(hypercube["x15"])/float(hypercube["w15"])
#    y = float(hypercube["y15"])/float(hypercube["w15"])
#    z = float(hypercube["z15"])/float(hypercube["w15"])
#    _vertex15_.pts = {"p1":x,"p2":y,"p3":z}
#def _vertex16_():
#    x = float(hypercube["x16"])/float(hypercube["w16"])
#    y = float(hypercube["y16"])/float(hypercube["w16"])
#    z = float(hypercube["z16"])/float(hypercube["w16"])
#    _vertex16_.pts = {"p1":x,"p2":y,"p3":z}
_vertex1_()
_vertex2_()
_vertex3_()
_vertex4_()
_vertex5_()
_vertex6_()
_vertex7_()
_vertex8_()
#_vertex9_()
#_vertex10_()
#_vertex11_()
#_vertex12_()
#_vertex13_()
#_vertex14_()
#_vertex15_()
#_vertex16_()
print( "\n","3D point 1",_vertex1_.pts,"\n","3D point 2",_vertex2_.pts,"\n","3D point 3",_vertex3_.pts,"\n","3D point 4",_vertex4_.pts,
       "\n","3D point 5",_vertex5_.pts,"\n","3D point 6",_vertex6_.pts,"\n","3D point 7",_vertex7_.pts,"\n","3D point 8",_vertex8_.pts,
# "\n","3D point 9",_vertex9_.pts,"\n","3D point 10",_vertex10_.pts,"\n","3D point 11",_vertex11_.pts,"\n","3D point 12",_vertex12_.pts,
#"\n","3D point 13",_vertex13_.pts,"\n","3D point 14",_vertex14_.pts,"\n","3D point 15",_vertex15_.pts,"\n","3D point 16",_vertex16_.pts
    )
def _3d_():         # 4 3D points per line to make it look complicated
    _3d_.tot = [_vertex1_.pts,_vertex2_.pts,_vertex3_.pts,_vertex4_.pts,_vertex5_.pts,_vertex6_.pts,_vertex7_.pts,_vertex8_.pts]
    _3d_.dat1 = _vertex1_.pts
    _3d_.dat2 = _vertex2_.pts
    _3d_.dat3 = _vertex3_.pts
    _3d_.dat4 = _vertex4_.pts
    _3d_.dat5 = _vertex5_.pts
    _3d_.dat6 = _vertex6_.pts
    _3d_.dat7 = _vertex7_.pts
    _3d_.dat8 = _vertex8_.pts
#    _3d_.dat9 = _vertex9_.pts
#    _3d_.dat10 = _vertex10_.pts
#    _3d_.dat11 = _vertex11_.pts
#    _3d_.dat12 = _vertex12_.pts
#    _3d_.dat13 = _vertex13_.pts
#    _3d_.dat14 = _vertex14_.pts
#    _3d_.dat15 = _vertex15_.pts
#    _3d_.dat16 = _vertex16_.pts