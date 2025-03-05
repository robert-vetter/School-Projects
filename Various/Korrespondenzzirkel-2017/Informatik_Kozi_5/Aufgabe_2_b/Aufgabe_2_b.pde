int x=0;
int y=0;
int abstand;
int a=500;


void setup(){
  size(500, 500);
  background(255,255,255);
}
void draw(){
   abstand=abstand+2;
    line(x, y, a, y);
    y=y+abstand;
  
}
