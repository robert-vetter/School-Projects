int x=50;
int y=110;
int laenge=20;
int abstand=10;


void setup(){
  size(500, 500);
  background(255,255,255);
}
void draw(){
  while(x <=300){
    line(x, y, x, y+laenge);
    x=x+abstand/2;
  }
}
