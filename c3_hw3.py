
from vpython import*

scene = canvas(width = 600 , height = 600 , center=vector(10,0,0), background=vector(0.6,0.8,0.8))

ball = sphere(radius=1, color=color.yellow, pos=vector(0,0,0), v=vector(0,6.0,0),a=vector(0,0,0),make_trail = True) 
dt = 0.001
t = 0.0
m = 1.0
F = vector(4.0,0,0)             
right = 0                   
left = 0                        

while True:                 
    rate(1/dt)
    t = t+dt
    ball.a = F/m
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt

    F_vec = ball.v.rotate(angle=radians(270))
    F = 4.0*norm(F_vec)
    
    if ball.v.x>=0 and ball.v.x+ball.a.x*dt<0:  
        right = ball.pos.x
    if ball.v.x<=0 and ball.v.x+ball.a.x*dt>0:
        left = ball.pos.x
        print ("theoretical radius = ", mag(ball.v)*mag(ball.v)*m/mag(F))    
        print ("simulated radius = " , abs(right-left)/2)    
