import math
from matplotlib.pyplot import *
from numpy import *
n=1.34
N=10
b=[11, 14, 23, 34, 40, 43, 46]
a=[15, 22.5, 30, 45, 60, 67.5,  75]
alpha=linspace(1, 89, N)
beta = zeros(len(alpha))
liste = [0,90]
gerade = [48, 48]
a1=[15, 30, 45, 60, 75]
b1=[10, 21, 32, 39, 46]

for i in range(len(alpha)):
	beta[i]= arcsin(sin(alpha[i]/180*3.14)*1/n)*180/3.14
	i=i+1

plot(a, b)
plot(a1, b1)
plot(alpha, beta)
plot(liste, gerade)
xlabel('a in Grad' )
ylabel('b in Grad')
show()
close()
