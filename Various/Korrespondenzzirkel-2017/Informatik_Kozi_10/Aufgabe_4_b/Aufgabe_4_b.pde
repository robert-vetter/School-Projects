float angle=20;
float Farbe1;
float Farbe2;
float Farbe3;
void setup(){
  size(600, 600);
  Farbe1=69;
Farbe2=139;
Farbe3=116;
}

void draw(){
  background(25);
  drawTriangle(width-110, height-550, width-90, height-560, width-90, height-540 );
 
}

void drawTriangle(float x1, float y1, float x2, float y2, float x3, float y3){
 
  triangle(x1, y1, x2, y2, x3, y3);
  translate(120, -80);
rotate(radians(angle));
    if(y1<600){
      fill(Farbe1, Farbe2, Farbe3);
    drawTriangle(x1/1.044, y1*1.5, x2, y2*1.5, x3, y3*1.5);
    }
 
}
