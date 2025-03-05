import math 
from matplotlib.pyplot import *
from numpy import *
t = 0
h=10
g=9.81 
vx=10 
N=int(input("Schritte: "))
tges=math.sqrt(2*h/g) 
sxw=vx*tges 
t = linspace(0, tges, N)
print(t)
print(round(tges,2))
print(round(sxw,2))
sx = zeros(N)
sy = zeros(N) 
for i in range(N):
		sy[i] = -0.5 * g* t[i]**2+h
		sx[i]=vx*t[i]
plot(t, sy)
xlabel('t in s')
ylabel('$sx$ in m')	
xlim (0, 10.2)
ylim(0, 1.45)	
show()
close()

plot(sx, sy)
xlabel('sx in m')
ylabel('h in m')
show()
close()
