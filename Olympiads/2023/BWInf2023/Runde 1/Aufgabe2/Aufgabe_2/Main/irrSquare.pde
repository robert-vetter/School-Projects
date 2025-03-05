class irrSquare{
  
  //Vier Eckpunkte des Polygons
  float x1;
  float y1;
  float x2;
  float y2;
  float x3;
  float y3;
  float x4;
  float y4;
  
  //Geschwindigkeiten nach links (vLeft), nach oben (vUp), nach rechts (vRight) sowie nach unten (vDown)
  float vLeft;
  float vUp;
  float vRight;
  float vDown;
  
  //Farbe der Vierecke
  color cl;

  //Booleans als Indikatoren für das Wachstum in die vier Richtungen
  boolean growingLeft = true;
  boolean growingRight = true;
  boolean growingUp = true;
  boolean growingDown = true;

  //Konstruktor um jeweiligen Objekte zu erstellen
  irrSquare(float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4, color cl, float vx1, float vy2, float vx3, float vy4){
    this.x1 = x1;
    this.y1 = y1;
    this.x2 = x2;
    this.y2 = y2;
    this.x3 = x3;
    this.y3 = y3;
    this.x4 = x4;
    this.y4 = y4;
    this.vLeft = vx1;
    this.vUp = vy2;
    this.vRight = vx3;
    this.vDown = vy4;
    this.cl = cl;
    
  }
  
  //Methode, die die jeweiligen Punkte mit der entsprechenden Geschwindigkeit bewegt
  void grow(){
    if (growingLeft){
          x1 -= vLeft;
    }
    if (growingUp){
          y2-=vUp;
    }
    if (growingRight){
          x3+=vRight;
    }
    if (growingDown){
          y4+=vDown;
    } 
  }
  
  //Methode, die für das kollidieren mit den Fenster-Begrenzungen verantwortlich ist
  int edges(){
    if (x1 < 0){
       return 0;
     } else if (y2 < 0){
       return 1;
     } else if (x3 > width){
       return 2;
     } else if (y4 > height){
       return 3;
     } else {
       return 4;
     }
  }
  
  //Methode, die die Vierecke auf das Canvas zeichnet
  void show(){
    fill(cl);
    quad(x1, y1, x2, y2, x3, y3, x4, y4);
  }
}
