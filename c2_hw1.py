from vpython import *

size=0.1
scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))
x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=size, color=color.yellow, pos=vector(0,0,0), v=vector(-2.0,0,0))
gd1 = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue, graph=gd1)
gd2 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="v")
f2 = gcurve(color=color.green, graph=gd2)
gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="a")
f3 = gcurve(color=color.red, graph=gd3)
t=0
dt=0.001
acc=vector(3.0, 0, 0)
while(t<5):
    rate(1/dt)
    t=t+dt
    if(ball.v.x+acc.x*dt>=0 and ball.v.x<0):
        print("t = %.2f" %t)
        print("x = %.2f" %ball.pos.x)
        print("v = %.2f" %ball.v.x)
    ball.v=ball.v+acc*dt
    ball.pos=ball.pos+ball.v*dt
    if(t+dt>=3 and t<3):
        print("t = %.2f" %t, "position = %.2f" %ball.pos.x)

    f1.plot(pos=(t, ball.pos.x))
    f2.plot(pos=(t, ball.v.x))
    f3.plot(pos=(t, acc.x))
