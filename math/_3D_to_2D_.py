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
# TODO: change 3D to 2D and display on a graph using turtle
# Use https://www.geeksforgeeks.org/python-get-first-and-last-elements-of-a-list/
from _4D_to_3D_ import _3d_

_3d_()

def _vertex1_():                                     # refer to /math/_4D_to_3D functions or the main readme for explaination
    x = float(_3d_.dat1["p1"])/float(_3d_.dat1["p3"])
    y = float(_3d_.dat1["p2"])/float(_3d_.dat1["p3"])
    _vertex1_.pts = {"x1":x,"y1":y,}
def _vertex2_():
    x = float(_3d_.dat2["p1"])/float(_3d_.dat2["p3"])
    y = float(_3d_.dat2["p2"])/float(_3d_.dat2["p3"])
    _vertex2_.pts = {"x1":x,"y1":y,}
def _vertex3_():
    x = float(_3d_.dat3["p1"])/float(_3d_.dat3["p3"])
    y = float(_3d_.dat3["p2"])/float(_3d_.dat3["p3"])
    _vertex3_.pts = {"x1":x,"y1":y,}
def _vertex4_():
    x = float(_3d_.dat4["p1"])/float(_3d_.dat4["p3"])
    y = float(_3d_.dat4["p2"])/float(_3d_.dat4["p3"])
    _vertex4_.pts = {"x1":x,"y1":y,}
def _vertex5_():
    x = float(_3d_.dat5["p1"])/float(_3d_.dat5["p3"])
    y = float(_3d_.dat5["p2"])/float(_3d_.dat5["p3"])
    _vertex5_.pts = {"x1":x,"y1":y,}
def _vertex6_():
    x = float(_3d_.dat6["p1"])/float(_3d_.dat6["p3"])
    y = float(_3d_.dat6["p2"])/float(_3d_.dat6["p3"])
    _vertex6_.pts = {"x1":x,"y1":y,}
def _vertex7_():
    x = float(_3d_.dat7["p1"])/float(_3d_.dat7["p3"])
    y = float(_3d_.dat7["p2"])/float(_3d_.dat7["p3"])
    _vertex7_.pts = {"x1":x,"y1":y,}
def _vertex8_():
    x = float(_3d_.dat8["p1"])/float(_3d_.dat8["p3"])
    y = float(_3d_.dat8["p2"])/float(_3d_.dat8["p3"])
    _vertex8_.pts = {"x1":x,"y1":y,}
def _vertex9_():
    x = float(_3d_.dat9["p1"])/float(_3d_.dat9["p3"])
    y = float(_3d_.dat9["p2"])/float(_3d_.dat9["p3"])
    _vertex9_.pts = {"x1":x,"y1":y,}
def _vertex10_():
    x = float(_3d_.dat10["p1"])/float(_3d_.dat10["p3"])
    y = float(_3d_.dat10["p2"])/float(_3d_.dat10["p3"])
    _vertex10_.pts = {"x1":x,"y1":y,}
def _vertex11_():
    x = float(_3d_.dat11["p1"])/float(_3d_.dat11["p3"])
    y = float(_3d_.dat11["p2"])/float(_3d_.dat11["p3"])
    _vertex11_.pts = {"x1":x,"y1":y,}
def _vertex12_():
    x = float(_3d_.dat12["p1"])/float(_3d_.dat12["p3"])
    y = float(_3d_.dat12["p2"])/float(_3d_.dat12["p3"])
    _vertex12_.pts = {"x1":x,"y1":y,}
def _vertex13_():
    x = float(_3d_.dat13["p1"])/float(_3d_.dat13["p3"])
    y = float(_3d_.dat13["p2"])/float(_3d_.dat13["p3"])
    _vertex13_.pts = {"x1":x,"y1":y,}
def _vertex14_():
    x = float(_3d_.dat14["p1"])/float(_3d_.dat14["p3"])
    y = float(_3d_.dat14["p2"])/float(_3d_.dat14["p3"])
    _vertex14_.pts = {"x1":x,"y1":y,}
def _vertex15_():
    x = float(_3d_.dat15["p1"])/float(_3d_.dat15["p3"])
    y = float(_3d_.dat15["p2"])/float(_3d_.dat15["p3"])
    _vertex15_.pts = {"x1":x,"y1":y,}
def _vertex16_():
    x = float(_3d_.dat16["p1"])/float(_3d_.dat16["p3"])
    y = float(_3d_.dat16["p2"])/float(_3d_.dat16["p3"])
    _vertex16_.pts = {"x1":x,"y1":y,}

_vertex1_()
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

def run():
    print("\n","2D point 1:",_vertex1_.pts["x1"],",",_vertex1_.pts["y1"],
        "\n","2D point 2:",_vertex2_.pts["x1"],",",_vertex2_.pts["y1"],
        "\n","2D point 3:",_vertex3_.pts["x1"],",",_vertex3_.pts["y1"],
        "\n","2D point 4:",_vertex4_.pts["x1"],",",_vertex4_.pts["y1"],
        "\n","2D point 5:",_vertex5_.pts["x1"],",",_vertex5_.pts["y1"],
        "\n","2D point 6:",_vertex6_.pts["x1"],",",_vertex6_.pts["y1"],
        "\n","2D point 7:",_vertex7_.pts["x1"],",",_vertex7_.pts["y1"],
        "\n","2D point 8:",_vertex8_.pts["x1"],",",_vertex8_.pts["y1"],
        "\n","2D point 9:",_vertex9_.pts["x1"],",",_vertex9_.pts["y1"],
        "\n","2D point 10:",_vertex10_.pts["x1"],",",_vertex10_.pts["y1"],
        "\n","2D point 11:",_vertex11_.pts["x1"],",",_vertex11_.pts["y1"],
        "\n","2D point 12:",_vertex12_.pts["x1"],",",_vertex12_.pts["y1"],
        "\n","2D point 13:",_vertex13_.pts["x1"],",",_vertex13_.pts["y1"],
        "\n","2D point 14:",_vertex14_.pts["x1"],",",_vertex14_.pts["y1"],
        "\n","2D point 15:",_vertex15_.pts["x1"],",",_vertex15_.pts["y1"],
        "\n","2D point 16:",_vertex16_.pts["x1"],",",_vertex16_.pts["y1"],
    )
def _2d_():         # 4 3D points per line to make it look complicated
    _2d_.dat1 = _vertex1_.pts
    _2d_.dat2 = _vertex2_.pts
    _2d_.dat3 = _vertex3_.pts
    _2d_.dat4 = _vertex4_.pts
    _2d_.dat5 = _vertex5_.pts
    _2d_.dat6 = _vertex6_.pts
    _2d_.dat7 = _vertex7_.pts
    _2d_.dat8 = _vertex8_.pts
    _2d_.dat9 = _vertex9_.pts
    _2d_.dat10 = _vertex10_.pts
    _2d_.dat11 = _vertex11_.pts
    _2d_.dat12 = _vertex12_.pts
    _2d_.dat13 = _vertex13_.pts
    _2d_.dat14 = _vertex14_.pts
    _2d_.dat15 = _vertex15_.pts
    _2d_.dat16 = _vertex16_.pts