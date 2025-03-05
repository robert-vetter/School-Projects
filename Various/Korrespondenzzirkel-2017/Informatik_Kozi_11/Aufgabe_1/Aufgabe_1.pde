void setup () {
size (640, 360);
noStroke ();
noLoop ();
}
void draw () {
drawCircle(width/2, 280, 8);
}
void drawCircle(int x, int radius , int level) {
float tt = 126 * level /4.0;
fill(tt);
ellipse(x, height/2, radius*2, radius *2);
if(level > 1) {
level = level - 1;
drawCircle(x - radius/2, radius/2, level );
drawCircle(x + radius/2, radius/2, level );
}
}

/* In setup() werden die generellen Informationen einmal abgearbeitet.
In draw() wird die Funktion "drawCircle" festgelegt und mit Werten versehen.
In der neu erstellten Funktion werden den Werten Variablen zugewiesen.
Zudem wird die neue Variable "tt", welche für die Farbe zuständi ist, ein Wert zugewiesen.
Dann wird eine Ellipse gezeichnet, bei der alle Eigenschaften außer die y-Höhe veränderbar sind.
Wenig später wird der Platzhalter "level" noch genauer bestimmt.
Dort wurde geschrieben, dass das Level sich stetig um eins absenken soll.
Der letzte Teil der if-Funktion besteht aus zwei Befehlen, welche die Größe und die Position der Ellipse genau festlegen.
Wenn man den Wert der Variable "level" verändert, ändert sich die Farbe der Kreise, die Größe der Ellipse, sowie die Position.*/
