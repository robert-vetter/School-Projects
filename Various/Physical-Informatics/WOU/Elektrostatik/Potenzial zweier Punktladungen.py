from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

r0 = 0.01 
rmax = 0.1
pi=np.pi
Q1= 10**-7 
Q2 = 10**-7
E0 = 8.854*10**-12
N = 70
Nd = 5
epr = 1

r1 = zeros([N, N])
r2= zeros([N, N])
P1 = zeros([N, N])
P2 = zeros([N, N])
E=zeros([N, N])
x0 = linspace(-rmax, rmax, N)
y0 = linspace(-rmax, rmax, N)

x,y=meshgrid(x0, y0)
plt.plot(x, y)



			
for i in range(N):
	for j in range(N):
		r1[i, j]= math.sqrt((x[i, j]-Nd*r0)**2 + y[i, j]**2)
		r2[i, j]= math.sqrt((x[i, j]+Nd*r0)**2 + y[i, j]**2)
		if r1[i, j] >= r0:
			P1[i, j]= Q1/(4*3.41**eprE0*r[i, j])
		else:
			P1[i, j] = Q1/(4*3.41*epr*E0*r0) 
		if r2[i, j] >= r0:
			P2[i, j]= Q2/(4*3.41*epr*E0*r[i, j])
		else:
			P2[i, j] = Q2/(4*3.41*E0*epr*r0)
		Pg[i, j]=P1[i, j] + P2[i, j]
		
dx = abs(x0[1]-x0[0])
dy=abs(y0[1]-y0[0])

#imshow(r)
#colorbar()
#plt.show()
#plt.close()

#plt.plot(E)
#plt.show()
#plt.close()

fig = plt.figure(figsize=(10, 10), dpi=3000)
EField = fig.gca(projection="3d")
EField.set_xlabel('x in m')
EField.set_ylabel('y in m')
EField.set_zlabel('z in V/m')

#Potential = fig.gca(projection='3d')
#Potential.set_xlabel('x in m')
#Potential.set_xlabel('y in m')
#Potential.set_xlabel('z in V/m')



surf=EField.plot_surface(x, y, E, rstride=1, cstride=1, cmap='jet', linewidth=0, edgecolor='none')
cbar=fig.colorbar(surf, shrink=0.5, aspect=15, orientation='horizontal')
cbar.set_label('$\phi$ in V')
show()
