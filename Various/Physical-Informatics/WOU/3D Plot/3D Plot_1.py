from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

r0 = 0.01 
rmax = 0.1
pi=np.pi
Q = 10**-7 #C
E0 = 8.854*10**-12
N = 70

r = zeros([N, N])
E=zeros([N, N])
x0 = linspace(-rmax, rmax, N)
y0 = linspace(-rmax, rmax, N)
x,y=meshgrid(x0, y0)
plt.plot(x, y)

#plt.show()
#print(x[0,0])
#print(y[0,0])
#print(x[N-1, N-1])
#print(y[N-1, N-1])
#print(x[N/2, N/2])
#print(y[N/2, N/2])

for i in range(N):
	for j in range(N):
		r[i, j]= math.sqrt(x[i, j]**2 + y[i, j]**2)
		if r[i, j] >= r0:
			E[i, j] = Q/(4*3.41*E0*r[i, j])
		else:
			E[i, j] = Q/(4*3.41*E0*r0) #physikalisch nicht korrekt, E muss null sein
		
		

				
print(r[0,0])
print(r[N-1, N-1])
print(r[N/2, N/2])
print(r[N-1, N/2])

imshow(r)
colorbar()
plt.show()
plt.close()

plt.plot(E)
plt.show()
plt.close()

fig = plt.figure(figsize=(10, 10), dpi=3000)
EField = fig.gca(projection="3d")

surf=EField.plot_surface(x, y, E, rstride=1, cstride=1, cmap='jet', linewidth=0, edgecolor='none')
plt.show()
