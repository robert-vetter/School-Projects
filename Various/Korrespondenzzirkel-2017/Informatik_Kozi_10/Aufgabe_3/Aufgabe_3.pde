float Farbe1;
float Farbe2;
float Farbe3;

void setup () {
size (410 ,300);

}

void draw(){
 
  background(25);
  drawRect(width-210, height-height, 200);
}

void drawRect(float x, float y, float d){
   float Farbe1=random(255);
  float Farbe2=random(255);
  float Farbe3=random(255);
 rect(x, y, d, d);
 if(d> 10){
   fill(Farbe1, Farbe2, Farbe3);
 drawRect(x-d/2, y, d/2);
 }
}
  
