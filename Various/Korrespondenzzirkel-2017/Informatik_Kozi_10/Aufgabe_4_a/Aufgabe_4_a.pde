float angle;
float Farbe1;
float Farbe2;
float Farbe3;

void setup(){
  size(300, 300);
Farbe1=random(255);
Farbe2=random(255);
Farbe3=random(255);
}

void draw(){
  background(25);

  drawRect(width-147.5, height-147.5, 137);
}

void drawRect(float x, float y, float d){
  angle=5;
  
  rect(x, y, d, d);
  if(d>25){
translate(14, -12.5);
    rotate(radians(angle));
rectMode(CENTER);
fill(Farbe1, Farbe2, Farbe3);
    drawRect(x, y, d/1.3);
  }
 
}
