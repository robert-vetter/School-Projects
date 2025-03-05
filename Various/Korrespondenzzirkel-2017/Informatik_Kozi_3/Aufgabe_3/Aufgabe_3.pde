
void setup(){
  size(500, 500);
 background(random(0, 255), random(0, 255), random(0, 255));
}

void draw(){
fill(random(0, 255),random(0, 255),random(0, 255));
rect(random(0, 400), random(0, 400), random(0, 100), random(0,100));

}


void keyPressed() {
  background(random(0, 255), random(0, 255), random (0, 255), random(0, 255));
}

/*Zuerst legt man in setup() die Größe des Skizzenfensters und den Hintergrund fest.
Danach überlegt man sich, wo überall die Rectecke hingezeichnet werden dürfen.
Danach überlegt legt man die werte für die Frabe fest, die im Bereich 0-255 liegen können.
Für Farbwerte darf man keine Dezimahlzahlen nehmen, sondern nur Ganzzahlen.
Dann initialisiert und deklariert man die Variablen.
Jetzt denkt man darüber nach, welche Werte man in draw() reinsetzt oder in andere Funktionen, wie z.B.
keyPressed() oder mousePressed(). Wenn die Rectecke wieder verschwinden sollen, habe ich das 
einfach so gemacht, dass ich in keyPressed() eingefügt habe, dass der Hintergrund dann in
einer zufälligen Farbe neu "aufgedeckt" wird.
Im Endeffekt bin ich sehr zufrieden mit dem Ergebnis und ichwüsste nicht richtig was ich hätte verbessern sollen. :)*/
