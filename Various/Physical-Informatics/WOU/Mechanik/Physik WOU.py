import math
g = 9.81 #m/s^2
h = 10 # m , int(input('Abwurfhöhe in m:'))
v0 = 10 # m/s, int(input('Abwurfgeschwindigkeit in m/s: '))
N = 30
t = 0
zaehler = 0
tges = math.sqrt(2*h / g)
dt = tges / N
sges = v0 * tges
print ('Weg gesamt:',round(sges, 2),'m')
print ('Zeit gesamt: ',round(tges, 2),'s')
print('Geschwindigkeit:',v0,'m/s')
for i in range(N):
	t1 = t + dt
	zaehler = zaehler + 1
	t = t1
	ds = v0 * t1
	print(zaehler,'. dx Weg', round(ds, 2), 'in m')
	print(zaehler,'. dt Zeit', round(t1, 2), 'in s')
	
	
	







