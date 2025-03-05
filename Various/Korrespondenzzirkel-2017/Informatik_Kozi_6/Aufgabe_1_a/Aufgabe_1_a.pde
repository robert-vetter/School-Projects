int x=0;
int speed=1;

void setup(){
  size(500, 500);
}

void draw(){
  background(255);
  bewegeBall();
  reflektiereBall();
  skizziereBall();
}


void bewegeBall(){
  x=x+speed;
}

void reflektiereBall(){
  if((x>width) || (x<0)){
    speed=speed*-1;
  }
}

void skizziereBall(){
  stroke(0);
  fill(175);
  ellipse(x, 100, 20, 20);
}

/*Wenn man in draw() den Namen ändert, genauso wie in der Prozedur 
  skizziereBall(), passiert nichts.*/
