# graphics-driver
A graphics driver made by an idiot for an idiot.
# Core features
Take a strictly defined 4d shape and put it on a 2d screen.
# Why?
I'm an insane idiot who happens to be somewhat smart in asking google for the answers.
# How?
It takes a 4d shape, converts it into 3d, then using steps explained [here](https://www.youtube.com/watch?v=C8YtdC8mxTU), it displays it on a 2d screen.
# In detail
I take a point defined in a list of variables x,y,z,w, then create a new list with orthogonal projection, ignoring w to create x,y,z. After that, I reduce the x,y,z proportional to a fraction  $$ 1 \over w $$
[how to make fractions](https://github.blog/2022-05-19-math-support-in-markdown/)
# Sources
Idea: No Source
How it works: https://forum.processing.org/one/topic/convert-4d-to-3d.html and https://researchblog.duke.edu/2017/04/26/visualizing-the-fourth-dimension/