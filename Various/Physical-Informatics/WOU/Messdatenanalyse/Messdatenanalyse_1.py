from numpy import *
from numpy.random import normal
import matplotlib.pyplot as plt



def mysnv(x, mean, sigma):
	y = 1/(sigma*sqrt(2*pi))*exp(-(x-mean)**2/(2*sigma**2))
	return y

def mymean(T):
	sum = 0
	for i in range(len(T)):
		sum += T[i]
	mit = round(sum/len(T),3)
	return mit

N = 1000
T = normal(loc=4,scale=1,size=N);

mymean = mymean(T)
sigmaT = std(T, ddof = 1)
DT = sigmaT/sqrt(N)
DTr = DT/mymean

print('Statistische Daten zur Messung')
print('------------------------------')
print('Mittelwert:', round(mymean,3), 's')
print('Absoluter Fehler', round(DT,3), 's')
print('Relativer Fehler', round(DTr*100,1), 's')
print('------------------------------')
print('Ergebnis: T=(',round(mymean,3),'+-',round(DT,3),') s')

x = linspace(min(T),max(T),N)
mypdf = zeros(N)
for i in range(N):
	mypdf[i] = mysnv(x[i],mymean,sigmaT)
	
A = linspace(1,N,N)
meanTplot = zeros(N)
meanAbsErrTplot = zeros(N)

for i in range (N-1):
	meanTplot[i+1] = mean(T[0:i+2])
	meanAbsErrTplot[i+1]=(std(T[0:i+2]))/sqrt(i+1)
	
plt.xlabel('Periodendauer T in x')
plt.ylabel('relative Häufigkeit')
plt.hist(T, bins=round(sqrt(N)), normed=True)

plt.plot(x,mypdf)
plt.show()
plt.close()

plt.errorbar(A[1:N], meanTplot[1:N], yerr=meanAbsErrTplot[1:N], capsize=4)
plt.plot([1, N], [mymean, mymean]);
plt.show()


# + eigene Definitionen von Standardabweichung, absoluter- und relativer Fehler
