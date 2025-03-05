void setup () {
size (300 ,300);
int x=width;
vertikal(x);
}


void vertikal (int xpos) {
if (xpos >1) {
int x= xpos/2;
line(x,0,x,height );
vertikal(x);
}
}

/*1a) Zuerst wird wieder getestet ob der xpos-Wert größer als 1 ist.
Da dies zutrifft, wird mit dem Programm fortgefahren. 
Eine neue Variable x wird mit dem Wert 300/2=150 initialisiert.
Demzufolge wird eine vertikale Linie vom Punkt (150/0) und (150/300) gezeichnet.
Jetzt sind wir beim zweiten Durchlauf. Da 150>1 ist, wird noch eine Linie vom Punkt
(75/0) zum Punkt (75/300) gezeichnet. Die x-Koordinate wird dann immer weiter halbiert, 
bis x kleiner gleich 1 erreicht wird. Wie man sieht, halbieren sich die Abstände, weil x auch
immer wieder halbiert wird. Danach endet das Programm.*/

/*2a) 1. In vertikal wird getestet, ob der übergebene Wert (xpos) größer als 1 ist. Da dieser 300 ist,
wird fortgefahren. Eine neue Variable x wird mit dem Wert 300 / 2 = 150 initialisiert.
Eine Linie wird vertikal vom Punkt (150/0) zum Punkt (150/300) gezeichnet. Danach wird
die Methode vertikal mit dem Wert 150 aufgerufen.
2. Nun sind wir wieder am Anfang der Methode. Es wird getestet, ob der übergebene Wert
größer 1 ist, dieser ist 150. Daher wird ein neues x mit dem Wert 150/2 = 75 initialisiert.
Eine Linie wird vertikal vom Punkt (75/0) zum Punkt (75/300) gezeichnet. Danach wird
die Methode vertikal mit dem Wert 75 aufgerufen.
...
Vorletzter Aufruf: Der übergebene Parameter ist noch größer 1, nämlich rund 1,17. x = 1,17 / 2 = 0,59. Eine Linie wird
vertikal vom Punkt (0,59/0) zum Punkt (0,59/300) gezeichnet. 
Letzter Aufruf: Da jetzt x<1 ist, endet der Aufruf hier. Die Fallunterscheidung wird damit übersprungen und die
Abarbeitung ist beendet. */
