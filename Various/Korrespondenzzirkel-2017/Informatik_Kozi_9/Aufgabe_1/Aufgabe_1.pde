Ameise[] Ameisen=new Ameise[10];

void setup(){
  size(600, 600);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i]=new Ameise();
  }
}
void draw(){
  background(255);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i].bewegen();
   Ameisen[i].display();
  }
}


class Ameise{
  float x;
  float y;
  float diameter;

  float yspeed;
  float xspeed;
  
  Ameise(){
    x=random(width);
    y=random(height);

  }
  
  void bewegen(){
   y =y+random(-2, 2);
    x=x+random(-2, 2);
     if (x > width) {
  x = 0;
} else if (x < 0) {
  x = width;
}
   if (y > height) {
  y = 0;
} else if (y < 0) {
  y = height;
}
  }
  void display(){
    fill(127, 100);
    ellipse(x-4, y-10, 5, 10);
    ellipse(x+4, y-10, 5, 10);
    rect(x-18, y-4, 10, 5);
    rect(x-18, y+4, 10, 5);
    rect(x+8, y-4, 10, 5);
    rect(x+8, y+4, 10, 5);
    ellipse(x, y, 20, 20);
    
  }
  
}
    
    
