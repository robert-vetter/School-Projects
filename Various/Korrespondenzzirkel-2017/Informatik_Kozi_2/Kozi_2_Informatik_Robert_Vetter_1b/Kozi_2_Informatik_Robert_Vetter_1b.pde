void setup() {
   size(400, 400);
   background(255);
}

void keyPressed() {
   background(255);
}


void draw(){
}

void mousePressed() {
   stroke(0);
   fill(175);
   rectMode(CENTER);
   rect(mouseX, mouseY, 10, 10);
}

/*Die Quadrate können gelöscht werden, indem man in der Prozedur keyPressed() noch ein background() hinzufügt.
Dadurch wird die Zeichenfläche dann wieder weiß gemacht. Es scheint, als wären die Quadrate verschwunden.*/
