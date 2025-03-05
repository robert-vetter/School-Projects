ArrayList<Ellipse> Ellipse1;
 
void setup() {
  size(300, 300);
  background(255, 255, 255);
  Ellipse1 = new ArrayList<Ellipse>();
}
 
void draw() {
  background(200);
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
    ellipse(x, y, 20, 20);   
  }
}

void mouseDragged(){
   Ellipse1.add(new Ellipse());
}
 
