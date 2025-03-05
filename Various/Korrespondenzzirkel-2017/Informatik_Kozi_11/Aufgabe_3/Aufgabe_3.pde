
float angle = 170;
float Astradius = 0.67;


void setup(){
  size(400,400);
}

void draw(){
  background(51);
  stroke(255);
  translate(width/2, height);
  Ast(100);
}

void Ast(float len){
  line(0,0,0,-len);
  translate(0, -len);
  if (len > 4){
    pushMatrix();
    rotate(angle);
    Ast(len * Astradius);
    popMatrix();
    pushMatrix();
    rotate(-angle);
    Ast(len * Astradius);
    popMatrix();
  }
}
