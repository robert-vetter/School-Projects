import math 
from matplotlib.pyplot import *
from numpy import *

anzahl = [0, 1, 2, 3, 4, 5, 6, 7]
spannungen = [5.1, 5.26, 5.44, 5.6, 5.8, 5.99, 6.30, 6.6]
x = flipud(spannungen)
dicke = 0.08
z=[]
for i in range(len(x)):
	y = anzahl[i] * 0.08
	z.append(y)
print(z)
legend()
plot(z, x,  'x')
plot(z, x,  '-')
plot([0, 0.6], [5.7, 5.7])
plot([0, 0.6], [5.7, 5.7])
plot([0, 0.6], [5.31, 5.31])
xlabel('Dicke in mm')
ylabel('Spannungen an Sekundärspule in V')
grid()
show()
