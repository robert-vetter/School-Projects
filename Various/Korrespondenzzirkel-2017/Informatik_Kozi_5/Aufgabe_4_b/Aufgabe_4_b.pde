int x;
int laenge=10;
int abstand=20;

void setup(){
  size(500, 500);
  background(255, 255, 255);
}
void draw(){
background(255, 255, 255);
   
      
    line(mouseX-40, mouseY-40, mouseX-40, mouseY+40);
    line(mouseX-20, mouseY-40, mouseX-20, mouseY+40);
    line(mouseX, mouseY-40, mouseX, mouseY+40);
    line(mouseX+20, mouseY-40, mouseX+20, mouseY+40);
    line(mouseX+40, mouseY-40, mouseX+40, mouseY+40);
    line(mouseX-40, mouseY-40, mouseX+40, mouseY-40);
    line(mouseX-40, mouseY-20, mouseX+40, mouseY-20);
    line(mouseX-40, mouseY, mouseX+40, mouseY);
    line(mouseX-40, mouseY+20, mouseX+40, mouseY+20);
    line(mouseX-40, mouseY+40, mouseX+40, mouseY+40);
}
