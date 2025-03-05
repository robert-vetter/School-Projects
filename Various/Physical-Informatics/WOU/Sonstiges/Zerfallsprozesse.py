from math import *
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 1


N_0 = 90
Lambda = 0.0130
h = 0.1
tmax = 250
n=int(round(tmax/h))

N = np.zeros(n+1)
N[0] = N_0
for i in range(n):
	N[i+1] = - Lambda * N[i] * h + N[i]	
t = np.linspace(0, tmax, n+1)
plt.plot(t,N, '-')
plt.xlabel('Zeit $t$')
plt.ylabel('Anzahl Kerne $N$')
#plt.show()





N_0 = 90
h = 0.1
n=int(round(tmax/h))
I = [90, 45, 26, 11, 8, 2]
tm = [0, 51, 100, 170, 200, 250]

N = np.zeros(n+1)
N[0] = N_0

for i in range(n):
	N[i+1] = -Lambda * N[i] * h + N[i]
	
t = np.linspace(0, tmax, n+1)
plt.plot(t,N, '-')
plt.plot(tm, I, 'x')
plt.xlabel('Zeit $t$')
plt.ylabel('Anzahl Kerne $N$')
plt.show()


