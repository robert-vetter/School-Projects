Ball meinBall;

 
void setup () {
  meinBall=new Ball();
  size(320, 240);
  smooth ();
  
}
 
void draw () {
  background (45);
  meinBall.zeichnen();
  meinBall.bewegen();
}

class Ball{


float xGeschwindigkeit = 2;
float yGeschwindigkeit = 2;
float durchmesser = 30;
float a=(random(0, width));
float b=(random(0, height));

  
 void bewegen(){
   
  
  if (a > width - durchmesser / 2) {
    xGeschwindigkeit = xGeschwindigkeit * -1;
  }
  if (a < durchmesser / 2) {
    xGeschwindigkeit = xGeschwindigkeit * -1;
  }
  if (b > height - durchmesser / 2) {
    yGeschwindigkeit = yGeschwindigkeit * -1;
  }
  if (b < durchmesser / 2) {
    yGeschwindigkeit = yGeschwindigkeit * -1;
  }
  a = a + xGeschwindigkeit;
  b = b + yGeschwindigkeit;
 }
 
 void zeichnen(){
  
  ellipse (a, b, durchmesser, durchmesser);
 }
}
