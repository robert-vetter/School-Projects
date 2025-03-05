int x=50;
int y=110;
int laenge=20;
int abstand=10;



void setup(){
  size(500, 500);
  background(255,255,255);
}
void draw(){
  
 for(int x=50; x<=150; x=x+abstand/2){
   line(x, y, x, y+laenge);
 }
 
}
