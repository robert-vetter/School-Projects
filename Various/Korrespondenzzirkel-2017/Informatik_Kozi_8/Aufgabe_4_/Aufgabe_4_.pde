
void setup(){
  size(1200, 600);
  background(255, 255, 255);
}


void draw(){
    translate(600,500);
  strokeWeight(5);
  for (int i=0; i<61; i++) {
    float x = 0.25 * (-pow(i,2) + 40*i + 1200)*sin((PI*i)/180);
    float y = -0.25 * (-pow(i,2) + 40*i + 1200)*cos((PI*i)/180);
    point(x,y); 
    point(-x,y); 
  }
 
     
   
  

}

//War echt schwierig :)
