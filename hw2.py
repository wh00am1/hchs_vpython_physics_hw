import numpy
from vpython import *

sz=0.05
x=arrow(pos=vec(0, 0, 0), axis=vec(1, 0, 0), shaftwidth=0.02, color=color.green)
y=arrow(pos=vec(0, 0, 0), axis=vec(0, 1, 0), shaftwidth=0.02, color=color.red)
z=arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 1), shaftwidth=0.02, color=color.blue)
s1=sphere(radius=sz, color=color.yellow, pos=vec(0, -1, 1), v=vec(-0.4, 1, -0.4))
s2=sphere(radius=sz, color=color.green, pos=vec(1, 1, 1), v=vec(-1.5, -0.5, -0.7))
dt=0.001
t=0.0
#for t in numpy.arange(0.0, 1.5, dt):
while(t<1.5):
    rate(1/dt)
    s1.pos=s1.pos+s1.v*dt
    s2.pos=s2.pos+s2.v*dt
    t=t+dt
print(s1.pos, s2.pos)
