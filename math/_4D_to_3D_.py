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
print("List of 4d points:", hypercube,"\n")
# converting 4d to 3d is the same as converting
# 3d to 2d, only one dimension louder.
# The simplest 3d to 2d case is using orthogonal
# projection and just ignoring z, you can do the
# same with 4d to 3d, just drop the last coord.
# Perspective transforms are the same, reduce the
# first three dimensions proportional to 1 / the    # Vertex function:
# fourth.                                           # First, don't create a var i of the 4D point, w. You
def _vertex1_():                                    # want to make stuff look more complicated than it is.
    p1 = int(hypercube["x1"])/int(hypercube["w1"])  # \
    p2 = int(hypercube["y1"])/int(hypercube["w1"])  #  } Divide x, y, and z by w
    p3 = int(hypercube["z1"])/int(hypercube["w1"])  # /
    _vertex1_.pts = [p1,p2,p3]                      # Create a not-so-local-var of the new 3D point for later
def _vertex2_():                                    # use OUTSIDE of the function, or in other words,"Do what
    p1 = int(hypercube["x2"])/int(hypercube["w2"])  # is not meant to be." Repeat 16 times.
    p2 = int(hypercube["y2"])/int(hypercube["w2"])
    p3 = int(hypercube["z2"])/int(hypercube["w2"])
    _vertex2_.pts = [p1,p2,p3]
def _vertex3_():
    p1 = int(hypercube["x3"])/int(hypercube["w3"])
    p2 = int(hypercube["y3"])/int(hypercube["w3"])
    p3 = int(hypercube["z3"])/int(hypercube["w3"])
    _vertex3_.pts = [p1,p2,p3]
def _vertex4_():
    p1 = int(hypercube["x4"])/int(hypercube["w4"])
    p2 = int(hypercube["y4"])/int(hypercube["w4"])
    p3 = int(hypercube["z4"])/int(hypercube["w4"])
    _vertex4_.pts = [p1,p2,p3]
def _vertex5_():
    p1 = int(hypercube["x5"])/int(hypercube["w5"])
    p2 = int(hypercube["y5"])/int(hypercube["w5"])
    p3 = int(hypercube["z5"])/int(hypercube["w5"])
    _vertex5_.pts = [p1,p2,p3]
def _vertex6_():
    p1 = int(hypercube["x6"])/int(hypercube["w6"])
    p2 = int(hypercube["y6"])/int(hypercube["w6"])
    p3 = int(hypercube["z6"])/int(hypercube["w6"])
    _vertex6_.pts = [p1,p2,p3]
def _vertex7_():
    p1 = int(hypercube["x7"])/int(hypercube["w7"])
    p2 = int(hypercube["y7"])/int(hypercube["w7"])
    p3 = int(hypercube["z7"])/int(hypercube["w7"])
    _vertex7_.pts = [p1,p2,p3]
def _vertex8_():
    p1 = int(hypercube["x8"])/int(hypercube["w8"])
    p2 = int(hypercube["y8"])/int(hypercube["w8"])
    p3 = int(hypercube["z8"])/int(hypercube["w8"])
    _vertex8_.pts = [p1,p2,p3]
#def _vertex9_():
#    p1 = int(hypercube["x9"])/int(hypercube["w9"])
#    p2 = int(hypercube["y9"])/int(hypercube["w9"])
#    p3 = int(hypercube["z9"])/int(hypercube["w9"])
#    _vertex9_.pts = [p1,p2,p3]
#def _vertex10_():
#    p1 = int(hypercube["x10"])/int(hypercube["w10"])
#    p2 = int(hypercube["y10"])/int(hypercube["w10"])
#    p3 = int(hypercube["z10"])/int(hypercube["w10"])
#    _vertex10_.pts = [p1,p2,p3]
#def _vertex11_():
#    p1 = int(hypercube["x11"])/int(hypercube["w11"])
#    p2 = int(hypercube["y11"])/int(hypercube["w11"])
#    p3 = int(hypercube["z11"])/int(hypercube["w11"])
#    _vertex11_.pts = [p1,p2,p3]
#def _vertex12_():
#    p1 = int(hypercube["x12"])/int(hypercube["w12"])
#    p2 = int(hypercube["y12"])/int(hypercube["w12"])
#    p3 = int(hypercube["z12"])/int(hypercube["w12"])
#    _vertex12_.pts = [p1,p2,p3]
#def _vertex13_():
#    p1 = int(hypercube["x13"])/int(hypercube["w13"])
#    p2 = int(hypercube["y13"])/int(hypercube["w13"])
#    p3 = int(hypercube["z13"])/int(hypercube["w13"])
#    _vertex13_.pts = [p1,p2,p3]
#def _vertex14_():
#    p1 = int(hypercube["x14"])/int(hypercube["w14"])
#    p2 = int(hypercube["y14"])/int(hypercube["w14"])
#    p3 = int(hypercube["z14"])/int(hypercube["w14"])
#    _vertex14_.pts = [p1,p2,p3]
#def _vertex15_():
#    p1 = int(hypercube["x15"])/int(hypercube["w15"])
#    p2 = int(hypercube["y15"])/int(hypercube["w15"])
#    p3 = int(hypercube["z15"])/int(hypercube["w15"])
#    _vertex15_.pts = [p1,p2,p3]
#def _vertex16_():
#    p1 = int(hypercube["x16"])/int(hypercube["w16"])
#    p2 = int(hypercube["y16"])/int(hypercube["w16"])
#    p3 = int(hypercube["z16"])/int(hypercube["w16"])
#    _vertex16_.pts = [p1,p2,p3]
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
def _3d_():         # 4 3D points per print function to make it look complicated
    print("3D point 1",_vertex1_.pts,"\n","3D point 2",_vertex2_.pts,"\n","3D point 3",_vertex3_.pts,"\n","3D point 4",_vertex4_.pts)
    print("3D point 5",_vertex5_.pts,"\n","3D point 6",_vertex6_.pts,"\n","3D point 7",_vertex7_.pts,"\n","3D point 8",_vertex8_.pts)
#    print("3D point 9",_vertex9_.pts,"\n","3D point 10",_vertex10_.pts,"\n","3D point 11",_vertex11_.pts,"\n","3D point 12",_vertex12_.pts)
#    print("3D point 13",_vertex13_.pts,"\n","3D point 14",_vertex14_.pts,"\n","3D point 15",_vertex15_.pts,"\n","3D point 16",_vertex16_.pts)
_3d_()