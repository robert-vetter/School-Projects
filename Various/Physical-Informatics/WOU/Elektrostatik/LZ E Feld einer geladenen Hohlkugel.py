import numpy as np
import matplotlib.pyplot as plt

r = 1 #cm
pi=np.pi
Q = 10**-7 #C
E0 = 8.854*10**-12
R=np.linspace(r, 20, 100)
E = Q/(4*3.41*E0*R*R)

plt.plot(R, E, "-")
plt.show()
