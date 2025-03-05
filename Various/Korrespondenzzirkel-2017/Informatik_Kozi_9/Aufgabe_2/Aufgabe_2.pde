Ameise[] Ameisen=new Ameise[10];
Futterquelle[] Futterquellen=new Futterquelle[3];

void setup(){
  size(600, 600);
  rectMode(CENTER);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i]=new Ameise();
  }
  for(int j=0; j<Futterquellen.length; j++){
    Futterquellen[j]=new Futterquelle();
  }
}
void draw(){
  frameRate(400);
  background(255);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i].bewegen();
   Ameisen[i].display();
   Ameisen[i].Futterquelle();
  
  }
  for(int j=0; j<Futterquellen.length; j++){
    Futterquellen[j].ZeichnenUndBewegen(); 
  }
}


class Ameise{
  float x;
  float y;
    float b;
    float c;
    float FutterquelleX;
    float FutterquelleY;

  
  Ameise(){
    b=random(500);
    c=random(700);
  x=random(b, 20)*width*1.3;
    y=random(c, 20)*height*1.3;
    FutterquelleX=random(width);
    FutterquelleY=random(height);     
  }
  
  void bewegen(){
  x=noise(b, 10)*width*1.3;
    y=noise(c, 30)*height*1.3;
    if (x > width) {
  x = 0;
} else if (x < 0) {
  x = width;
}
   if (y > height) {
  y = 0;
} else if (y < 0) {
  y = height;
}
 b=b+0.0015;
 c=c+0.0015;
  }
  
  void Futterquelle(){
    
      }
    
  void display(){
     fill(127, 100);
    ellipse(x-4, y-10, 5, 10);
    ellipse(x+4, y-10, 5, 10);
    rect(x-14, y-4, 10, 5);
    rect(x-14, y+4, 10, 5);
    rect(x+16, y-4, 10, 5);
    rect(x+16, y+4, 10, 5);
    ellipse(x, y, 20, 20);
    fill(139, 90, 43);
     ellipse(width/2, height/2, 60, 60);
  }
}

class Futterquelle{
  float FutterquelleX;
   float FutterquelleY;
  float Size;
  float radius2;
   
   Futterquelle(){
     FutterquelleX=random(width);
      FutterquelleY=random(height);
      Size=20;
     
   }
   void ZeichnenUndBewegen(){
       fill(255, 126, 37);
     ellipse(FutterquelleX, FutterquelleY, Size, Size);
     Size++;
   
    if(Size==50){
     Size--;
    }   
  }
}
