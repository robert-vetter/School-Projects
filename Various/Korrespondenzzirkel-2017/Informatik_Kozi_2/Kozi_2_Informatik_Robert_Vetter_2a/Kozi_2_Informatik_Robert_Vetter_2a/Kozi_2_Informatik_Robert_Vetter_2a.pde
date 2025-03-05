void setup() {
size (320, 500);
noSmooth ();
background (255, 255, 255);
ellipseMode(RADIUS);
}


void draw() {
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
ellipse (125, 90, 12, 17); //linke Auge
ellipse (175, 90, 12, 17); //rechtes Auge
fill (0);
ellipse (150, 135, 20, 5); //Mund
}
