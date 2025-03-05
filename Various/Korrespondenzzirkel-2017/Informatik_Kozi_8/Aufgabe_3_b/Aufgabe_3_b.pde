ArrayList<Ellipse> Ellipse1;
float Farbe1=(random(255));
float Farbe2=(random(255));
float Farbe3=(random(255));
void setup() {
  size(500, 500);
  background(255, 255, 255);
  background(255, 255, 255);
  Ellipse1 = new ArrayList<Ellipse>();
}
 
void draw() {
  
  for (int i = 0; i < Ellipse1.size(); i ++) {
    Ellipse part = Ellipse1.get(i);
    part.display();   
     
  }
}
 
class Ellipse {
  int x, y;
  Ellipse() {
    x = mouseX;
   y = mouseY;
}
 
  void display() {
    fill(Farbe1, Farbe2, Farbe3);
    ellipse(x, y, 20, 20);   
  }
}

void mouseDragged(){
   Ellipse1.add(new Ellipse());
}
