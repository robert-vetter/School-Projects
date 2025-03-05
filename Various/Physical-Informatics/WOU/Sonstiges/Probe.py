n = int(input("n: "))
print("Primfaktorzerlegung von", n, ":") 
zaehler = 0
z=n
i=2
a =""
if n > 2:
	while i<=n:
		if n%i == 0:
			zaehler = zaehler + 1 
			print(n, ":", i, "=", n/i ) 
			n = n/i
			a =a+str(i)+"*"
	else:
		i = i+1
		print(n, ":", i, "geht nicht") 
	print(z, "=", a)
else:
	print("Nicht möglich")
if zaehler > 1:
	print(z, "ist keine Primzahl")
else:
	print("Primzahl, da nur eine Ausgabe")
