import numpy as np
import matplotlib.pyplot as plt 

N=1000000
alpha=45/180*np.pi
v0=100/3.6
g=9.81
tw=int(input("Wurfdauer:"))


t=np.linspace(0,tw,N)
#v0x=np.cos(alpha)*v0
#v0y=np.sin(alpha)*v0


sx=v0*t*np.cos(alpha)
sy=v0*t*np.sin(alpha)-(g/2)*t**2


v0x=sx/t

v0y=(sy+(g/2)*t**2)/t
vy=v0y-g*t

plt.plot(sx,sy,"-")
plt.xlabel('Sx')
plt.ylabel('Sy')
plt.ylim(0)
plt.show()
plt.close()

plt.plot(t,vy,"-")
plt.xlabel('t')
plt.ylabel('vy')
plt.show()
plt.close()

plt.plot(t,v0x,"-")
plt.xlabel('t')
plt.ylabel('vx')
plt.show()
plt.close()

