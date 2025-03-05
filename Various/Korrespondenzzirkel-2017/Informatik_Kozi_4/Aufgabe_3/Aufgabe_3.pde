float x = 100;  
float y = 100;  
float w = 300;  
float h = 300; 
float a = 0;
float b = 0;
float c = 500;
float d = 500;
 
void setup () {
  size(500, 500);
 
}
 
void draw () {
  rect (x, y, w, h);
 
}

void mousePressed(){
   
if(mouseX > a && mouseX < a + c) {   
    if (mouseY > b && mouseY < b + d) {
     fill (100, 100, 100);
    rect (x, y, w, h); 
    background(255);
      
    }
  }
   if (mouseX > x && mouseX < x + w) {   
    if (mouseY > y && mouseY < y + h) {
     
     fill(255, 255, 255);
     rect (x, y, w, h);
  }
  }
  if (mouseX > x && mouseX < x + w) {   
    if (mouseY > y && mouseY < y + h) {
      background (255, 0, 0);
     fill(255, 255, 255);
     rect (x, y, w, h);
  }
  } 
}
