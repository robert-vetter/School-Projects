int x;
int y;
int a;
int b;

void setup(){
  size(500, 500);
  x=0;
  y=0;
  a=500;
  b=0;

}

void draw(){
  background(255);
  line(x, y, a, b);
  if(y==500){
  y=0;
  b=0;
  }
  y=y+1;
  b=b+1;
}
  
