from vpython import*	

size = 0.1    
v_0 = 1    

scene = canvas(center = vector(0,sqrt(3),0), background=vec(0.6,0.8,0.8))
ant1 = sphere(radius=size, color=color.yellow, pos=vec(2,0,0), v=vec(0,0,0), make_trail = True)
ant2 = sphere(radius=size, color=color.red, pos=vec(-2,0,0), v=vec(0,0,0), make_trail = True)
ant3 = sphere(radius=size, color=color.blue, pos=vec(0,2*sqrt(3),0), v=vec(0,0,0), make_trail = True)    


dt = 0.001	
t = 0.0		

while(mag(ant1.pos-ant2.pos)>0.01 and mag(ant2.pos-ant3.pos)>0.01 and mag(ant1.pos-ant3.pos)>0.01): 
    rate(1/dt)      
    t = t+dt
    
    ant1.v = norm(ant2.pos-ant1.pos)*v_0    
    ant2.v = norm(ant3.pos-ant2.pos)*v_0
    ant3.v = norm(ant1.pos-ant3.pos)*v_0
    
    ant1.pos = ant1.pos + ant1.v*dt    
    ant2.pos = ant2.pos + ant2.v*dt  
    ant3.pos = ant3.pos + ant3.v*dt

print ("相聚時間：" , t)
