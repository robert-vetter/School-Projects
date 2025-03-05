
float xpos;
float ypos;
float xGeschwindigkeit = 2;
float yGeschwindigkeit = 2;
float durchmesser = 30;
 
void setup () {
  size(320, 240);
  smooth ();
  xpos = width / 2;
  ypos = height / 2;
}
 
void draw () {
  background (45);
  if (xpos > width - durchmesser / 2) {
    xGeschwindigkeit = xGeschwindigkeit * -1;
  }
  if (xpos < durchmesser / 2) {
    xGeschwindigkeit = xGeschwindigkeit * -1;
  }
  if (ypos > height - durchmesser / 2) {
    yGeschwindigkeit = yGeschwindigkeit * -1;
  }
  if (ypos < durchmesser / 2) {
    yGeschwindigkeit = yGeschwindigkeit * -1;
  }
  xpos = xpos + xGeschwindigkeit;
  ypos = ypos + yGeschwindigkeit;
  ellipse (xpos, ypos, durchmesser, durchmesser);
}
