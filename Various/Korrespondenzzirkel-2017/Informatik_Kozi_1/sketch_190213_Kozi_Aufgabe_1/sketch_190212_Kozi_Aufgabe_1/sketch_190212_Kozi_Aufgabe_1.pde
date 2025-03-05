// Robert Vetter
size (320, 500);
noSmooth ();
/* Die Anweisung noSmooth() bewirkt, dass alle Geometrien und Schriftarten
auf der Leinwand mit gezackten Kanten dargestellt werden. Dadurch wirkt
das Bild unschärfer. */
background (255, 255, 255);
ellipseMode(RADIUS);
/*"Background" entscheidet über den Hintergrund und dessen Farbe. Es gibt drei Farbkanäle.
Der erste entscheidet über die Farbe rot, die weiteren über grün und blau. Die Zahlen von
0 bis 255 entscheiden über die Stärke des Farbtons. Wenn der Wert 0 lautet, wird die
Farbe überhaupt nicht in die Farbmischung miteinbezogen. Jedoch wenn der Wert z.B.
255 ist, wird die Farbe mit voller Stärke genutzt.*/
/* Der Ursprung der Ellipse wird durch die Funktion "ellipseMode (Radius)" geändert .
"ellipseMode (Radius) verwendet die ersten beiden Angaben auch als Mittelpunkt der Form, 
die letzten beiden jedoch um die Höhe und die Breite der Form zu bestimmen. Sonst
wurden die letzten beide Werte genutzt um den Durchmesser anzuzeigen, jetzt jedoch
werden sie genutzt um den Radius anzuzeigen. Im Ergebnis werden die Ellipsen 
doppelt so groß. */
fill (127, 255, 0);
rect (125, 75, 50, 150); //Körper
fill (255, 255, 255);
line (175, 225, 200, 250); //rechtes Bein
ellipse (150, 100, 45, 45); //Kopf
line (125, 225, 100, 250); //linkes Bein
line (125, 175, 100, 150); //linker Arm
line (175, 175, 200, 150); //rechter Arm
fill (204, 102, 0);
ellipse (150, 110, 7, 7); //Nase
fill (153);
noStroke () ; 
/* Stroke gibt an, wie die Farbe von den Rändern sein soll. Diesen Befehl
benötige ich aber nicht, weil ich noStroke schon so verlegt habe, dass
die Beine und Arme noch da sind. */
ellipse (125, 90, 12, 17); //linke Auge
ellipse (175, 90, 12, 17); //rechtes Auge
fill (0);
ellipse (150, 135, 20, 5); //Mund
triangle (130, 135, 140, 130, 125, 125); //linker Mundwinkel
triangle (170, 135, 160, 130, 175, 125); //rechter Mundwinkel
/* Alles was hinter der Anweisung noStroke steht, wird ohne Umriss gezeichnet. 
Das betrifft geometrische Formen aber auch Linien. */
