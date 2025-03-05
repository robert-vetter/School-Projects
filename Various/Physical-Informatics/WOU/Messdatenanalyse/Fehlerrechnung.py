from numpy import *
from numpy.random import normal
import matplotlib.pyplot as plt

N = 1000
T = normal(loc=4, scale=1, size=N)

plt.xlabel("Periodendauer T in s")
plt.ylabel("relative Häufigkkeit")
plt.hist(T, bins=round(sqrt(N)), normed=True)

meanT=mean(T)
sigmaT=std(T, ddof=1)
DT=sigmaT/sqrt(N)
DTr=DT/meanT

print("Statistische Daten zur Messung")
print("------------------------------")
print("Mittelwert:", round(meanT, 3), "s")
print("Absoluter Fehler:",round(DT, 3), "s")
print("Relativer Fehler:", round(DTr*100, 1), "%")
print("------------------------------")
print("Ergebnis: T=(", round(meanT, 3), "+-", round(DT, 3), ")s")


def mysnv(x, mean, sigma):
	y=1/(sigma*sqrt(2*pi))*exp(-(x-mean)**2/(2*sigma**2))
	return y
	
def mymean(T):
	s=0
	for i in range(len(T)):
		s = s + T[i]
	mean = s/len(T)
	print("Mein brechneter Mittelwert", round(mean, 3))
print(mymean(T))
	
x = linspace(min(T), max(T), N)
mypdf=zeros(N)

for i in range(N):
	mypdf[i]=mysnv(x[i], meanT, sigmaT)


plt.plot(x, mypdf)
plt.show()
plt.close()
