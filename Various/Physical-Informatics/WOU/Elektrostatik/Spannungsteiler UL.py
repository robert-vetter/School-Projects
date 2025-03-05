import math 
from matplotlib.pyplot import *
from numpy import *
R = 100
Rl1 = 10000000
R1 = [0, 40, 60, 80, 100] 
N = len(R1)
U0 = 20
Ul = zeros(N) 
R2 = zeros(N)

for i in range(N):
	R2[i] = R - R1[i]
	Ul[i] = (U0 * R1[i])/(R1[i]+R2[i]+(R1[i]*R2[i])/Rl1)
plot(Rl, Ul)
xlabel('Ul in V')
ylabel('R1 in Ohm')	
show()
close()


