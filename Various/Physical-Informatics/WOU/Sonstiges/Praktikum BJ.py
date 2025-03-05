#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math 
from matplotlib.pyplot import *
from numpy import *


# x-Werte
anzahl = 1000
# linspace(von, bis, Anzahl)
x=np.linspace(-5, 7, anzahl)

# y-Werte
# Gleichung
y1 = x*x - 2*x - 15



plot(x, y1)
xlabel('x')
ylabel('y')	
show()
close()



