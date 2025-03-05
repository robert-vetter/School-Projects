Flugzeug meinFlugzeug;
float a=random(800);
float b=random(800);
float c=random(800);
float d=random(800);
float e=random(800);

float f=random(255);
float g=random(255);
float h=random(255);
float i=random(255);
float j=random(255);


void settings(){
   size(800, 800);
}

void setup(){
  meinFlugzeug=new Flugzeug();
 background(255);
}

void draw(){
   meinFlugzeug.zeichnen();
  
}
  
class Flugzeug{
  float xPos1;
  float yPos1;
  float xPos2;
  float yPos2;
   float xPos3;
  float yPos3;
  float xPos4;
  float yPos4;
  float xPos5;
  float yPos5;
  
  Flugzeug(){
    xPos1=a;
    yPos1=a;
    yPos2=b;
    yPos2=b;
     xPos3=c;
    yPos3=c;
    yPos4=d;
    yPos4=d;
     yPos5=e;
    yPos5=e;
  }
  void zeichnen(){
  fill(f);
  rect(xPos1+25, yPos1-5, 5, 40);                     //Rad 3, 4
  rect(xPos1+175, yPos1-5, 5, 40);                     //Rad 1, 2
  ellipse(xPos1+200, yPos1+15, 30, 30);                  //Cockpit
  rect(xPos1, yPos1, 200, 30);                    //Flugzeugrumpf
  triangle(xPos1+75, yPos1, xPos1+125, yPos1, xPos1+75, yPos1-165);      //Flügel oben
  triangle(xPos1+75, yPos1+30, xPos1+125, yPos1+30, xPos1+75, yPos1+175);     //Flügel unten
       
   fill(g);
  rect(xPos2+25, yPos2-5, 5, 40);                     //Rad 3, 4
  rect(xPos2+175, yPos2-5, 5, 40);                     //Rad 1, 2
  ellipse(xPos2+200, yPos2+15, 30, 30);                  //Cockpit
  rect(xPos2, yPos2, 200, 30);                    //Flugzeugrumpf
  triangle(xPos2+75, yPos2, xPos2+125, yPos2, xPos2+75, yPos2-165);      //Flügel oben
  triangle(xPos2+75, yPos2+30, xPos2+125, yPos2+30, xPos2+75, yPos2+175);     //Flügel unten     
  
   fill(h);
  rect(xPos3+25, yPos3-5, 5, 40);                     //Rad 3, 4
  rect(xPos3+175, yPos3-5, 5, 40);                     //Rad 1, 2
  ellipse(xPos3+200, yPos3+15, 30, 30);                  //Cockpit
  rect(xPos3, yPos3, 200, 30);                    //Flugzeugrumpf
  triangle(xPos3+75, yPos3, xPos3+125, yPos3, xPos3+75, yPos3-165);      //Flügel oben
  triangle(xPos3+75, yPos3+30, xPos3+125, yPos3+30, xPos3+75, yPos3+175);     //Flügel unten  
  
   fill(i);
  rect(xPos4+25, yPos4-5, 5, 40);                     //Rad 3, 4
  rect(xPos4+175, yPos4-5, 5, 40);                     //Rad 1, 2
  ellipse(xPos4+200, yPos4+15, 30, 30);                  //Cockpit
  rect(xPos4, yPos4, 200, 30);                    //Flugzeugrumpf
  triangle(xPos4+75, yPos4, xPos4+125, yPos4, xPos4+75, yPos4-165);      //Flügel oben
  triangle(xPos4+75, yPos4+30, xPos4+125, yPos4+30, xPos4+75, yPos4+175);     //Flügel unten  
  
   fill(j);
  rect(xPos5+25, yPos5-5, 5, 40);                     //Rad 3, 4
  rect(xPos5+175, yPos5-5, 5, 40);                     //Rad 1, 2
  ellipse(xPos5+200, yPos5+15, 30, 30);                  //Cockpit
  rect(xPos5, yPos5, 200, 30);                    //Flugzeugrumpf
  triangle(xPos5+75, yPos5, xPos5+125, yPos5, xPos5+75, yPos5-165);      //Flügel oben
  triangle(xPos5+75, yPos5+30, xPos5+125, yPos5+30, xPos5+75, yPos5+175);     //Flügel unten  
}
}
