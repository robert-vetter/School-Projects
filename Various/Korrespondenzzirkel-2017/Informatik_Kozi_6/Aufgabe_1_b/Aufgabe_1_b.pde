int y=0;
int Geschwindigkeit=1;  //Initialisierung

void setup(){
  size(500, 500);       //Fenstereinstellungen
}

void draw(){
  background(255);
  bewegeQuadrat();
  reflektiereQuadrat();  //Prozeduren festgelegt
  zeichneQuadrat();
}

void bewegeQuadrat(){    //Bewegung der Form
  y=y+Geschwindigkeit;
}

void reflektiereQuadrat(){
  if((y>height) || (y<0)){
    Geschwindigkeit=Geschwindigkeit*-2;  //Reflektion des Quadrat am Ende des Fensters
  }
}

void zeichneQuadrat(){
  fill(100);
  rect(230, y, 40, 40);
}
