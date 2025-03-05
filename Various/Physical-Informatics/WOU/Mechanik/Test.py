import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
fig, ax = plt.subplots()
fig = plt.figure()

#Eingabe der Werte 

#y = float(raw_input("Bitte geben sie eine Abwurfhoehe, die größer als 0m ist, an: "))
#m = float(raw_input("Bitte geben sie eine Masse des Wurfkoerpes in kg an: "))
#a = float(raw_input("Bitte geben sie einen Abwurfwinkel zwischen 0° und 90° an: "))
#v = float(raw_input("Bitte geben sie eine Abwurfgeschwindigkeit in m/s an: "))

#Beispielwerte
y = 50
m = 0.5
a = 30
v = 100

#Berechnung Gesamtflugdauer
g = float(9.81)
t = v * np.sin(a * np.pi/180) / g
#print "\n=> Gesamtflugdauer = " , t , "s"

#Berechnung Maximale Höhe h
h = 0.5*g*t**2+y

#Berechnung Maximale Wurfweite w
w = (v*np.cos(a * np.pi/180) * (v * np.sin(a * np.pi/180)+ np.sqrt(v**2 * np.sin(a * np.pi/180)**2 + 2*g*y)))/g

print("\n=> Maximale Wurfweite =" , round(w,2) , "m")
print("=> Maximale Wurfhoehe =" , round(h,2) , "m")

def Wurfbahn(x):
	return (-(g/(2*v**2*np.cos(a * np.pi/180)**2))*x**2)+(np.tan(a * np.pi/180)*x+y)

#Darstellung der Funktion
x = np.arange(0.0,1000,1)
ax.plot(x,Wurfbahn(x),'r--')
ax.plot(w,0,'bo')
#ax.plot(w/2,h,'bo') #Hochpunkt

#Animation

#Skalierung der Achsen
ax.set_ylim(0, h + (0.1*h))
ax.set_xlim(0, w + (0.1*w))

#Achsenbeschriftung
ax.set_title('Schiefer Wurf')
ax.set_xlabel('Wurfweite [m]')
ax.set_ylabel('Wurfhoehe [m]')

plt.show()
