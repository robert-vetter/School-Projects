void setup() {
size(300, 300);
background(255);
}

void draw() {
ellipseMode(CENTER);
ellipse(pmouseX, pmouseY, 1, 1);
}

/*Wenn man eine Kurve "malen" will, brauch man in setup() erstmal die Standardanweisungen die genau einmal ausgeführt werden.
In draw() habe ich es so gelöst, dass ich mir erstmal überlegt habe aus was eine Kurve besteht. Ich kam darauf, dass sie aus 
kleinen Punkten zusammengesetzt ist. Da mir ein Punkt aber zu klein war, habe ich dafür sehr kleine Ellipsen verwendet*/
