void setup() {
size (320, 500);
noSmooth ();
background (255, 255, 255);
ellipseMode(RADIUS);

}

void draw() {
fill (127, 255, 0);  
rect (mouseX, mouseY, 50, 150); //Körper
fill (255);
ellipse (mouseX+25, mouseY+25, 45, 45); //Kopf
line (mouseX+50, mouseY+150, mouseX+75, mouseY+175); //rechtes Bein
line (mouseX, mouseY+150, mouseX-25, mouseY+175); //linkes Bein
line (mouseX, mouseY+100, mouseX-25, mouseY+75); //linker Arm
line (mouseX+50, mouseY+100, mouseX+75, mouseY+75); //rechter Arm
fill (204, 102, 0);
ellipse (mouseX+25, mouseY+35, 7, 7); //Nase
fill (153);
ellipse (mouseX+50, mouseY+15, 12, 17); //rechte Auge
ellipse (mouseX, mouseY+15, 12, 17); //linke Auge
fill (0);
ellipse (mouseX+25, mouseY+50, 20, 5); //Mund
}
/*Setup() bewirkt, dass in dieser Prozedur alle Anweisungen genau einmal ausgeführt werden.
Draw() bewirkt, dass alle Anweisungen in dieser Prozedur fortlaufend ausgeführt werden.*/
