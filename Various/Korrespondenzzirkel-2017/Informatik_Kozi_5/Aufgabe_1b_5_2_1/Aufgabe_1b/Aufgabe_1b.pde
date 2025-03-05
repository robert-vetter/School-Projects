int x=50;
int y=110;
int laenge=20;
int abstand=10;



void setup(){
  size(700, 700);
  background(255,255,255);
}
void draw(){
  do{
    line(x, y, x, y+laenge);
    x=x+abstand/2;
    
    
  }
  while(x <=150);
}
