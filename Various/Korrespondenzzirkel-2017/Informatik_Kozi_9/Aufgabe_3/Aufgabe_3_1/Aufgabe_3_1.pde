Ameise[] Ameisen=new Ameise[10];
Futterquelle[] Futterquellen=new Futterquelle[3];

void setup(){
  size(600, 600);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i]=new Ameise();
  }
  for(int j=0; j<Futterquellen.length; j++){
    Futterquellen[j]=new Futterquelle();
  }
}
void draw(){
  background(255);
  for(int i=0; i<Ameisen.length; i++){
    Ameisen[i].bewegendisplayFutterquelle();
   
  }
  for(int j=0; j<Futterquellen.length; j++){
    Futterquellen[j].ZeichnenUndBewegen(); 
  }
}


class Ameise{
  float x;
  float y;

  Ameise(){
    x=random(width);
    y=random(height);
  }
  
  void bewegendisplayFutterquelle(){
   y =y+random(-6, 6);
    x=x+random(-6, 6);
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
  
  if(x<150+10 && x>150-10 && y<150+10 && y>150-10){
   x=150;
     y=150;}
      if(x<530+20 && x>530-20 && y<420+20 && y>420-20){
   x=530;
     y=420;}
     if(x<360+10 && x>360-10 && y<360+10 && y>360-10){
   x=360;
     y=360;}
 
    fill(127, 100);
    ellipse(x-4, y-10, 5, 10);
    ellipse(x+4, y-10, 5, 10);
    rect(x-18, y-4, 10, 5);
    rect(x-18, y+4, 10, 5);
    rect(x+8, y-4, 10, 5);
    rect(x+8, y+4, 10, 5);
    ellipse(x, y, 20, 20);
    fill(205, 133, 63);
   ellipse(width/2, height/2, 50, 50);
    
    
  }
}
    
class Futterquelle{
  float FutterquelleX1;
   float FutterquelleY1;
   float FutterquelleX2;
   float FutterquelleY2;
   float FutterquelleX3;
   float FutterquelleY3;
  float Size;
  
   
   Futterquelle(){
     FutterquelleX1=150;
      FutterquelleY1=150;
      FutterquelleX2=530;
  FutterquelleY2=420;
   FutterquelleX3=360;
   FutterquelleY3=360;
      Size=20;
     
   }
   void ZeichnenUndBewegen(){
       fill(255, 126, 37);
     ellipse(FutterquelleX1, FutterquelleY1, Size, Size);
      ellipse(FutterquelleX2, FutterquelleY2, Size, Size);
       ellipse(FutterquelleX3, FutterquelleY3, Size, Size);
     Size++;
   
    if(Size==50){
     Size--;
    }   
  }
}
