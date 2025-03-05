float a;
float b;
float c;
float d;
float e;
float f;
float g;
float h;
float i;
float j;
float z;
float y;
float x;
float r;
float k;
float l;
float m;
float n;
void keyPressed(){
 
  if(keyCode==LEFT)
  a=a-15;
  if(keyCode==RIGHT)
  a=a+15;
}


void setup(){
 
  size(500, 500);
  
  a=205;
  b=485;
  c=90;
  d=15;
 e=random(500);
  h=random(500);
  i=20;
  j=30;
  z=random(500);
  y=random(500);
  x=random(500);
  r=random(500);
   k=random(500);
  l=random(500);
  m=random(500);
  n=random(500);
  
}

void draw(){
  background(255);
 
  
  
  f=f+2;
  ellipse(h, i, j, j);
  if(i==500){
  i=0;
  h=e;
  e=z;
  z=y;
  y=x;
  x=r;
  r=k;
  k=l;
  l=m;
  m=n;
  
  }
    i=i+2;
    
  
  
  fill(255, 48, 48);
  rect(a, b, c, d);
  if(f==500){
   
}
}

/* 3c) Man könnte das Problem mit der Kelle und dem Regentropfen so lösen, dass wenn ein Punkt auf der gesamten Breite der Kelle mit dem
x-Wert des Mittelpunkts des Regentropfens überneinstimmt, dass als richtiger Treffer bzw. ein Punkt gezählt wird.
Es müssen aber nicht nur die x-Werte übereinstimmen, sondern auch der y-Wert 500 in einem Skizzenfenster der Größe 500x500.
Dies könnte man so in einer if-Funktion schreiben:
if(f==500){
  hit=true
}
Danach könnte man auch weiterschreiben, dass wenn der Treffer richtig ist, zum dem jetzigen Punktestand 1 addiert wird.
Zudem müsste man jetzt auch noch die x-Position in dem "Quelltext" unterbringen.
Dies könnte man so schreiben (eventuell ist die Syntax falsch, sollte nur zur Veranschaulichung gedacht sein :)):
if(xposition ellipse(e, f, g, g)==xposition rect(a, b, c, d){
  hit=true
}
Jetzt müsste man eine Logische UND Verknüpfuung erstellen, dass wenn beide Teilaussagen richtig sind die Aussage wahr ist.
Sonst ist sie falsch.*/
