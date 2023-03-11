#!/usr/bin/env python3
from vpython import *
g = 9.8                 
size = 0.5              
height = 15.0           
m = 1.0                 

Fg = vector(0, -m*g, 0)

scene = canvas(width=600, height=600,x=0, y=0, center=vector(0, height/2, 0), background=color.black) 
floor = box(length=20, height=0.01, width=10, texture=textures.stucco)  	
ball = sphere(radius = size, color=color.blue, make_trail= True, trail_type="curve")
ball2 = sphere(radius = size, color=color.green, make_trail= True, trail_type="curve")

ball.pos = vector(0, 0, 0)    
ball2.pos = vector(0, 0, 0)    
ball.v = vector(20*cos(30*pi/180), 20*sin(30*pi/180), 0)            
ball2.v = vector(20*sin(30*pi/180), 20*cos(30*pi/180), 0)            

dt = 0.001	
t, t2 = 0.0, 0.0
maxt, maxh, dx, maxt2, maxh2, dx2=0, 0, 0, 0, 0, 0
while(ball.pos.y>=0):    
    ball.a = Fg/m       
    rate(1/dt)    
    t = t + dt
    if(ball.v.y>=0 and ball.v.y+ball.a.y*dt<0):
        maxh=ball.pos.y
    ball.v = ball.v + ball.a*dt          
    ball.pos = ball.pos + ball.v * dt    
while(ball2.pos.y>=0):    
    ball2.a = Fg/m       
    rate(1/dt)    
    t2 = t2 + dt
    if(ball2.v.y>=0 and ball2.v.y+ball2.a.y*dt<0):
        maxh2=ball2.pos.y
    ball2.v = ball2.v + ball2.a*dt          
    ball2.pos = ball2.pos + ball2.v * dt  
dx, dx2=ball.pos.x, ball2.pos.x
maxt, maxt2=t, t2
print("30度的飛行時間 =", maxt)
print("30度的最大高度 =", maxh)
print("30度的水平射程 =", dx)
print("60度的飛行時間 =", maxt2)
print("60度的最大高度 =", maxh2)
print("60度的水平射程 =", dx2)
