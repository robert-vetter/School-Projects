import math 
from matplotlib.pyplot import *
from numpy import *

Rl = [51, 100, 510, 1000, 5100, 1000000]
Ul = [4, 4.96, 6.26, 6.46, 6.64, 6.68]
U2 = [6.66, 6.66, 6.66, 6.66, 6.66, 6.66]


semilogx(Rl, Ul)
semilogx(Rl, U2)
xlabel('R in Ohm')
ylabel('U in V')
show()

