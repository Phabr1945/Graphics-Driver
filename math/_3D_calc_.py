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
from turtle import *

_3d_()

def _3D_to_2D_():
    def _3D_vertex1_():
        x1 = [_3d_.dat1[0]]
        for i in range(0, len(x1)):
            x1[i] = float(x1[i])
        y1 = [_3d_.dat1[1]]
        for i in range(1, len(y1)):
            y1[i] = float(y1[i])
        z1 = [_3d_.dat1[2]]
        for i in range(2, len(z1)):
            z1[i] = float(z1[i])
        print(x1)
        x = x1/z1
        y = y1/z1
        print(x,y)
    _3D_vertex1_()
_3D_to_2D_()