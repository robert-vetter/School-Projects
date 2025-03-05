float x=0;
float y=250;
float w=250;
float h=250;
float a=0;
float b=0;
float c=250;
float d=250;
float f=250;
float g=0;
float j=250;
float i=250;


void setup(){
  size(500, 500);
  background(255);
}

void draw(){
 
   
  rect(250, 0, 250, 250);
  rect(250, 250, 250, 250);
     rect(0, 0, 250, 250);
rect(0, 250, 250, 250);
      
 

         

  if (mouseX > x && mouseX < x + w) {   
    if (mouseY > y && mouseY < y + h) {
       
    fill (0, 255, 255);
   rect(0, 250, 250, 250);
    fill(0, 0, 255);
       
    }
  }     

 if(mouseX > a && mouseX < a + c) {   
    if (mouseY > b && mouseY < b + d) {
     
    fill (0, 255, 255);
    rect(0, 0, 250, 250);
     fill(0, 0, 255);   
  }     
}
 if(mouseX > f && mouseX < f + j) {   
    if (mouseY > g && mouseY < g + i) {
      
    fill (0, 255, 255);
     rect(250, 0, 250, 250);
 fill(0, 0, 255);
     
    }
  }    
 if(mouseX > i && mouseX < i + i) {   
    if (mouseY > i && mouseY < i + i) {
      fill (0, 255, 255);
     rect(250, 250, 250, 250);
 fill(0, 0, 255);
      
    }
  }
}


    
