from numpy import *
from pylab import *
from numpy.random import normal
import matplotlib.pyplot as plt

#Konstanten
m = 80
alpha = 30
g = 9.81
cW = 1.4
rho_L = 1.29
A=5
mü = 0.05
FH=m*g*sin(alpha/180*pi)
FR=m*g*cos(alpha/180*pi)*mü

N = 100
tmax=50
t=linspace(0, tmax, N)
dt=tmax/N

v=zeros(N)
a=zeros(N)
s=zeros(N)
FG=zeros(N)
FL=zeros(N)
for i in range(N-1):
	FG[i]=FH-FR-FL[i]
	a[i]=FG[i]/m
	v[i+1]=a[i]*dt+v[i]
	s[i+1]=v[i]*dt +s[i]
	FL[i+1]=0.5*cW*A*rho_L*v[i+1]**2
	

plt.plot(t, v)
xlabel("Zeit in h")
ylabel("Geschwindigkeit in m/s")
plt.show()
close()

plt.plot(t, s)
xlabel("Zeit in h")
ylabel("Strecke in m")
plt.show()
close()

plt.plot(t, FG)
xlabel("Zeit in h")
ylabel("Gesamtkraft in N")
plt.show()
close()

plt.plot(t, FL)
xlabel("Zeit in h")
ylabel("Luftwiderstand in Newton")
plt.show()
close()
