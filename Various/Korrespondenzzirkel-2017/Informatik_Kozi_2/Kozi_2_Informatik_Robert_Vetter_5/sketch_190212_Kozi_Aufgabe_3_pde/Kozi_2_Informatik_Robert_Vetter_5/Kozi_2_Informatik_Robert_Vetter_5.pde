// Robert Vetter
void setup() {
size (800, 500);
fill(127, 255, 0);
rect (525, 240, 200, 150); //Haus
fill (224, 255, 255);
ellipse (568, 105, 20, 100); //Rauch
fill (238, 64, 0);
rect (560, 160, 15, 50); //Schornstein
fill (255, 0, 0);
triangle (525, 240, 725, 240, 625, 140); // Dach
fill (0, 255, 255);
ellipse (625, 200, 35, 35); //Bullauge Dach 
fill (238, 64, 0);
rect (615, 340, 30, 50); //Tür
fill (255, 20, 147);
rect (670, 270, 30, 30); //Fenster rechts
fill (255,20, 147);
rect (550, 270, 30, 30); //Fenster links
fill (238,173,14);
rect (300, 300, 25, 90); //Baumstamm
fill (238,173,14);
rect (100, 300, 25, 90); //Baumstamm
fill (0,139, 0);
ellipse (112, 240, 120, 120); //Baumkrone
fill (0, 139, 0);
ellipse (312, 240, 120, 120); //Baumkrone
fill(255, 255, 0);
line (230, 100, 300, 160); //Sonnenstrahl re un
line (230, 100, 230, 190);//Sonnenstrahl un
line (230, 100, 330, 100);//Sonnenstrahl re
line (230, 100, 160, 160); //Sonnenstrahl li un
line (230, 100, 130, 100);//Sonnenstrahl li
line (230, 100, 300, 40); //Sonnenstrahl re ob
line (230, 100, 230, 10);//Sonnenstrahl ob
line (230, 100, 160, 40); //Sonnenstrahl li ob*/
fill (255, 255, 0);
ellipse (230, 100, 70, 70); //Sonne
line (0, 390, 800, 390); //Erdboden
}

void keyPressed(){
fill(mouseX, 213, mouseY);
ellipse (568, 105, 20, 100); //Rauch
fill (mouseX, 102, 255, mouseX);
rect (300, 300, 25, 90); //Baumstamm
fill (mouseY, 205, 102, mouseX);
rect (100, 300, 25, 90); //Baumstamm
fill (mouseX, 139, mouseY);
ellipse (112, 240, 120, 120); //Baumkrone
fill (mouseY, 255, 255, mouseX);
ellipse (230, 100, 70, 70); //Sonne
}

void mousePressed(){
fill (mouseY, 8, 255, mouseX);
rect (525, 240, 200, 150); //Haus
fill (mouseY, 189,2 , mouseX);
triangle (525, 240, 725, 240, 625, 140); // Dach
fill(mouseX, 27, mouseY);
rect (560, 160, 15, 50); //Schornstein
fill(mouseY, 67, 67, mouseX);
ellipse (625, 200, 35, 35); //Bullauge Dach 
fill (mouseX, 238, 64, mouseY);
rect (615, 340, 30, 50); //Tür
fill (mouseX, 20, 147, mouseY);
rect (670, 270, 30, 30); //Fenster rechts
fill (mouseY,020, 147, mouseX);
rect (550, 270, 30, 30); //Fenster links
fill (mouseX, 139, 50, mouseX);
ellipse (312, 240, 120, 120); //Baumkrone
}


void draw(){
}
