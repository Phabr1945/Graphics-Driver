# Graphics-Driver
A graphics driver made by an idiot for an idiot.
# Core features
Take a strictly defined 4d shape and put it on a 2d screen.
# Why?
I'm an insane idiot who happens to be somewhat smart in asking google for the answers.
# How?
It takes a 4d shape, converts it into 3d, then using steps explained [here](https://www.youtube.com/watch?v=C8YtdC8mxTU), it displays it on a 2d screen.
# In detail
I take a point defined in a list of variables x,y,z,w, then create a new list with orthogonal projection, ignoring w to create x,y,z. After that, I reduce the x,y,z proportional to a fraction  1/w. Look at example 1.
[how to make fractions](https://github.blog/2022-05-19-math-support-in-markdown/)
# examples
## Example 1:
point values:
```
_example_4D_point_ = {
    "x": 1,
    "y": 1,
    "z": 1,
    "w": 1,
}
```
point conversion and illegal python move
```
def _example_point_1_():
    p1 = x / w
    p2 = y / w
    p3 = z / w
    _example_point_1_.pts = [p1,p2,p3]
```
run the function to use a local var outside of the function
```
_example_point_1_()
```
print the converted point values
```
print("3D point 1",_example_point_1_.pts)
```
*output:*
```
> 3D point 1 [1.0, 1.0, 1.0]
```
# Sources
* Idea: No Source
* How it works: https://forum.processing.org/one/topic/convert-4d-to-3d.html and https://researchblog.duke.edu/2017/04/26/visualizing-the-fourth-dimension/
### License:
```
Graphics-Driver: A graphics driver made by an idiot for an idiot.
Copyright (C) <2024>  <Ryan Britton Maxson, Phbar1945, Райан Махъссон>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
```