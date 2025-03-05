class Circle{
  float x;
  float y;
  float r;
  color cl;

  boolean growing = true;
  
  Circle(float x, float y, color cl){
    this.x = x;
    this.y = y;
    this.cl = cl;
    r = 1;
    
  }
  
  void grow(){
    if (growing){
          r=r+3;
    }
  }
  
  boolean edges(){
    return (x+r > width || x - r < 0 || y +r > height || y - r < 0);
    
  }
  
  
  void show(){
    ellipse(x, y, r*2, r*2);
    fill(cl);
  }
  
}
