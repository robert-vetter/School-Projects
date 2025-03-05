Ball meinBall;

void settings(){
  size(400, 300);
}

void setup(){                
  meinBall= new Ball();
}

void draw(){
   background(255);
   meinBall.zeichnen();
   meinBall.bewegen();
   meinBall.prellen();
}

class Ball {
  color farbe;
  float xPos;
  float yPos;
  float geschwindigkeit;
  float gravitation;
  
  Ball(){
    farbe= #FFFE34;
    xPos=width/2;
    yPos=height/2;
    geschwindigkeit=0;
    gravitation=0.1;
}

void zeichnen(){                 
  fill(farbe);
  ellipse(xPos, yPos, 32, 32);

}

void bewegen(){              
  yPos=yPos+geschwindigkeit;
  geschwindigkeit=+geschwindigkeit+gravitation;
  }
  
void prellen(){             
  if(yPos>height){
    yPos=height;
    geschwindigkeit=geschwindigkeit*-0.7;
  }
}
}
