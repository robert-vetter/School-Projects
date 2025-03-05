Auto[] Autos= new Auto[30];

void setup() {
  size(1200, 1200);
  
  
  for (int i = 0; i < Autos.length; i++) {
    Autos[i] = new Auto(); 
  }  
}

void draw() {
  background(255);
   for (int i = 0; i < Autos.length; i++) {
   Autos[i].display();
   Autos[i].move();
   }
}
    

class Auto{
  float x;
  float y;
  int sizeReifen;
  float speedX;
   float speedY;
   float Farbe1;
   float Farbe2;
   float Farbe3;
  
  Auto(){
    x=random(width);
    y=random(height);
    sizeReifen=10;
    speedX=random(-3, 3);
    speedY=random(-3, 3);
    Farbe1=random(255);
   Farbe2=random(255);
   Farbe3=random(255);
    
  }
  
  void move(){
    x=x+speedX;
    y=y+speedY;
    
    
  }
  void display(){
    fill(Farbe1, Farbe2, Farbe3);
     ellipse(x, y, sizeReifen, sizeReifen); 
     ellipse(x+20, y, sizeReifen, sizeReifen);
     rect(x-2, y-20, 23,10);
  } 
    
}    
    
