Ball[] balls = new Ball[10];
 
void setup(){
  size(800, 800);
  for(int i=0; i<balls.length; i++){
    balls[i]= new Ball();
    
  }
}

void draw(){
  background(255);
  for(int i=0; i<balls.length; i++){
   balls[i].l();
    balls[i].display();
  }
}


class Ball{
  float x;
  float y;
  int size;
  float speedX;
  float speedY;
  
  Ball(){
    x=random(width);
    y=random(height);
    size=50;
    speedX=2;
    speedY=2;
  }
  
  void l(){
    x=x+speedX;
    if(x>width|| (x <0)){
      speedX=speedX*-1;
    }
    
      y=y+speedY;
    if(y>height|| (y <0)){
      speedY=speedY*-1;
    }
    }
  
  
  void display(){
    noStroke();
    fill(255, 0, 0);
    ellipse(x, y, size, size);
  }
}
