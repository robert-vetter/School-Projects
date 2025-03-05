import math 
from matplotlib.pyplot import *
#print("dieses programm dient zur Berechnung der Charaktika eines Körpers bei Würfen")
h=10#int(input("Bitte die Abwurfhöhe in m eingeben: ")) # in m
g=9.81 #in m/s^2
vx=10 #int(input("Bitte die Abwurfgeschwindigkeit in m/s eingeben: ")) #in m/s
t0=0 #in s
N=int(input("Bitte Anzahl der Zeitschritte eingeben: "))
tges=math.sqrt(2*h/g) #Berechnung der Wurfzeit
sxw=vx*tges #Berechnung der Wurfweite
print(round(tges,2))
print(round(sxw,2))
dt=tges/N
t = t0
for i in range(N):
	
	#if N==N:
		#print("der Körper liegt.")
		#break
	#else:
		t=t+dt
		sy=-0.5*g*t**2+h
		sx=vx*t
		vy=g*t
		plot (sx, h - sy, 'o-')
		ylabel('$s_x$ in m')
		xlabel('t in s')
		print("Bei der Zeit " ,round(t,2), " in s hat der körper" ,round(sy,2)," m Höhe und hat sich " ,round(sx,2)," m vom Abwurfpunkt entfernt und ist ",round(vy,2)," m/s in vertikaler Richtung schnell.")
	#print(round(t and sy, 2)
show()
