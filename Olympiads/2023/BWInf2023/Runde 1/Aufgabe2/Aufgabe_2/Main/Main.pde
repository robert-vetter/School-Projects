//Zusätzliche Informationen werden unten in der Konsole ausgegeben

//Parameter
boolean manualMode = false; //mithilfe des manuellen Modus können eigene Vierecke gezeichnet werden und so die genaue Position der Keime festgelegt werden

int n = 1000;//Anzahl an maximal erscheinenden Vierecken

//nur im Simulationsmodus verfügbar
float time = 0.5; //Jede (time/60)s wird ein neuer Keim geschaffen

float vmax = 0.1; //Maximale Wachstumsgeschwindigkeit 
float vmin = 0.05; //Minimale Wachstumsgeschwindigkeit 

//nur im Simulationsmodus verfügbar
int selection = 1; //Auswahl = 1: Muster wie in Aufgabe, Auswahl = 2: zufälliges Muster, Auswahl = 3: senkrechte Vierteilung, Auswahl = 4: Aufteilung in Quadranten


//Beginn des eigentlichen Programms
//Liste von Objekten initialisieren(Viereck)
ArrayList<irrSquare> irrSquares;

//Farbe initialisieren
color cl;

//Geschwindigkeit
float vLeft;
float vUp;
float vRight;
float vDown;

//Vektoren zur Überprüfung, ob Viereck in schon bestehendem Viereck erscheint
PVector[] vektoren = new PVector[4];

//Variable, die zur Klassifizierung der Screenshots verwendet wird
int num = 0;

//Variable, die Unterbrechung der Simulation angibt
boolean paused = false;

//Variable, die angibt, ob die Maus geklickt wurde
boolean varMouseClicked = false;

//Ortskoordinaten für die Vierecke
float x1;
float y1;
float x2;
float x3;
float x4;
float y2;
float y3;
float y4;

//jede timeX Sekunden wird ein neuer Keim generiert
float timeX = time/60;

void setup(){
  //grundlegende Eigenschaften festlegen
  size (800, 500);
  background(150, 150, 150);
  strokeWeight(0.05);
  frameRate(100);
  
  //Hinweise für den Benutzer ausgeben
  if(manualMode){
    println("Sie befinden sich im manuellen Modus und können nun selber unter Betätigung der linken Maustaste Vierecke zeichnen");
  } else {
    println("Sie befinden sich im Simulationsmodus");
    println("Es werden insgesamt " + n + " Vierecke gezeichnet");
    println("Jede " + nf(timeX, 0, 4) + " Sekunden wird ein neuer Keim generiert");
    println("Sie haben das Muster " + selection + " gewählt");
  }
  println("Für einen Screenshot müssen Sie auf die Simulation klicken, anschließend 's' drücken und zuletzt den entsprechenden Ordner auswählen, in welchem der Screenshot gespeichert werden soll (am besten derselbe Ordner wie diese Datei).");
  println("Für eine Unterbrechung bzw. Fortsetzung der Simulation sollten Sie wiederum auf die Simulation klicken und anschließend 'p' drücken");
  
  //neue ArrayList erstellen
  irrSquares = new ArrayList<irrSquare>();
  
  //zu dieser ArrayList ein neues Viereck mit den passenden Parametern hinzufügen
  irrSquares.add(new irrSquare(x1, y1, x2, y2, x3, y3, x4, y4, cl, vLeft, vUp, vRight, vDown));
}

//Hauptmethode, in welcher Polygone der Array-List hinzugefügt werden und auf Kollisionen überprüft wird
void draw(){
  
  irrSquare newIS = newIrrSquare();  
    if(!manualMode){
      //wenn nicht mehr als n Elemente enthalten sind, ein neues unregelmäßiges Viereck newIS gezeichnet wurde sowie Erscheinungszeit zutrifft, dann soll neues Viereck der ArrayList hinbzugefügt werden
      //Simulationsmodus
      if (newIS!=null && irrSquares.size() < n+1 && round(frameCount % time) == 0){
          irrSquares.add(newIS);
        }
    } else {
      //wenn nicht mehr als n Elemente enthalten sind, ein neues unregelmäßiges Viereck newIS gezeichnet wurde sowie Maus gedrückt wurde, dann soll neues Viereck der ArrayList hinbzugefügt werden
      //manueller Modus
      if (newIS!=null && irrSquares.size() < n+1 && mousePressed){
          irrSquares.add(newIS);
        }
     }
    
    //for-Schleife, die für jedes Viereck ausgeführt wird
    for (irrSquare p : irrSquares){
      //solange sich mindestens eine Ecke des Viereck noch ausbreitet:
      if (p.growingLeft || p.growingRight || p.growingUp || p.growingDown){
        
        //wenn die linke Ecke eine Begrenzung trifft, stoppe das Wachstum nach links
        if (p.edges() == 0){
          p.growingLeft = false;
        }
        //wenn die obere Ecke eine Begrenzung trifft, stoppe das Wachstum nach oben
        if (p.edges() == 1){
          p.growingUp = false;
        }
        //wenn die rechte Ecke eine Begrenzung trifft, stoppe das Wachstum nach rechts
        if (p.edges() == 2){
          p.growingRight = false;
        }
        
        //wenn die untere Ecke eine Begrenzung trifft, stoppe das Wachstum nach unten
        if (p.edges() == 3){
          p.growingDown = false;
        }
        
        //für die Variable "other" in der ArrayList
        for (irrSquare other : irrSquares){
          //wenn "other" ein anderes Viereck als "p" beschreibt
          if (p != other){
              //Puffer implementieren, um Ausgabe visuell hübscher zu machen
              float buffer = 0.1;
              //Überprüfung auf Kollision
              //Linke Ecke eines Vierecks berührt die rechte obere Seite eines anderen Vierecks
              float dL1 = dist(p.x1, p.y1, other.x3, other.y3);
              float dL2 = dist(p.x1, p.y1, other.x2, other.y2);
              float dLlineLen1 = dist(other.x2, other.y2, other.x3, other.y3);
              if (dL1 + dL2 >= dLlineLen1 - buffer && dL1 + dL2 <= dLlineLen1 + buffer){
                  p.growingLeft = false;
                  other.growingUp = false;
                  other.growingRight = false;
              }
              //Linke Ecke eines Vierecks berührt die rechte untere Seite eines anderen Vierecks
              float dL3 = dist(p.x1, p.y1, other.x3, other.y3);
              float dL4 = dist(p.x1, p.y1, other.x4, other.y4);
              float dLlineLen2 = dist(other.x3, other.y3, other.x4, other.y4);
              if (dL3 + dL4 >= dLlineLen2 - buffer && dL3 + dL4 <= dLlineLen2 + buffer){
                  p.growingLeft = false;
                  other.growingDown = false;
                  other.growingRight = false;
                }
              //Obere Ecke eines Vierecks berührt die rechte untere Seite eines anderen Vierecks
              float dT1 = dist(p.x2, p.y2, other.x3, other.y3);
              float dT2 = dist(p.x2, p.y2, other.x4, other.y4);
              float dTlineLen1 = dist(other.x3, other.y3, other.x4, other.y4);
              if (dT1 + dT2 >= dTlineLen1 - buffer && dT1 + dT2 <= dTlineLen1 + buffer){
                  p.growingUp = false;
                  other.growingDown = false;
                  other.growingRight = false;
              }
              //Obere Ecke eines Vierecks berührt die linke untere Seite eines anderen Vierecks
              float dT3 = dist(p.x2, p.y2, other.x1, other.y1);
              float dT4 = dist(p.x2, p.y2, other.x4, other.y4);
              float dTlineLen2 = dist(other.x1, other.y1, other.x4, other.y4);
              if (dT3 + dT4 >= dTlineLen2 - buffer && dT3 + dT4 <= dTlineLen2 + buffer){
                  p.growingUp = false;
                  other.growingDown = false;
                  other.growingLeft = false;
              }
              //Rechte Ecke eines Vierecks berührt die linke obere Seite eines anderen Vierecks
              float dR1 = dist(p.x3, p.y3, other.x1, other.y1);
              float dR2 = dist(p.x3, p.y3, other.x2, other.y2);
              float dRlineLen1 = dist(other.x1, other.y1, other.x2, other.y2);
              if (dR1 + dR2 >= dRlineLen1 - buffer && dR1 + dR2 <= dRlineLen1 + buffer){
                  p.growingRight = false;
                  other.growingUp = false;
                  other.growingLeft = false;
              }
              //Rechte Ecke eines Vierecks berührt die linke untere Seite eines anderen Vierecks
              float dR3 = dist(p.x3, p.y3, other.x1, other.y1);
              float dR4 = dist(p.x3, p.y3, other.x4, other.y4);
              float dRlineLen2 = dist(other.x1, other.y1, other.x4, other.y4);
              if (dR3 +dR4 >= dRlineLen2 - buffer && dR3 + dR4 <= dRlineLen2 + buffer){
                  p.growingRight = false;
                  other.growingDown = false;
                  other.growingLeft = false;
              }
              //Untere Ecke eines Vierecks berührt die rechte obere Seite eines anderen Vierecks
              float dB1 = dist(p.x4, p.y4, other.x2, other.y2);
              float dB2 = dist(p.x4, p.y4, other.x3, other.y3);
              float dBlineLen1 = dist(other.x2, other.y2, other.x3, other.y3);
              if (dB1 +dB2 >= dBlineLen1 - buffer && dB1 + dB2 <= dBlineLen1 + buffer){
                  p.growingDown = false;
                  other.growingRight = false;
                  other.growingUp = false;
              }
              //Untere Ecke eines Vierecks berührt die linke obere Seite eines anderen Vierecks
              float dB3 = dist(p.x4, p.y4, other.x1, other.y1);
              float dB4 = dist(p.x4, p.y4, other.x2, other.y2);
              float dBlineLen2 = dist(other.x1, other.y1, other.x2, other.y2);
              if (dB3 +dB4 >= dBlineLen2 - buffer && dB3 + dB4 <= dBlineLen2 + buffer){
                  p.growingDown = false;
                  other.growingLeft = false;
                  other.growingUp = false;
              }
                 
            }
          }
        }
        
        //führe durchgängig die Methoden für das Zeichnen und für das Wachstum aus
        p.show();
        p.grow();
      
    }
  }

//wird aufgerufen, wenn Maustaste geklickt wird
void mouseClicked(){
   varMouseClicked = true;
}

//wird aufgerufen, wenn Maustaste gehalten wird
void mousePressed(){
  varMouseClicked = true;
}
  
irrSquare newIrrSquare(){
  
   //zufällige Koordinaten des Ursprungs, wenn der Simulationsmodus aktiviert ist
   if(!manualMode){
      x1 = random(width);
      y1 = random(height);
      x2 = x1;
      x3 = x2;
      x4 = x3;
      y2 = y1;
      y3 = y2;
      y4 = y3;
   }
   
   //Zeichnen der Vierecke im manuellen Modus
   if(varMouseClicked  && mouseButton == LEFT){
     x1 = mouseX;
     y1 = mouseY;
     x2 = x1;
     x3 = x2;
     x4 = x3;
     y2 = y1;
     y3 = y2;
     y4 = y3;
   }
   
   //initialisieren und deklarieren der Farbe
   int cl = 100;
   
   vLeft = random(vmin, vmax);
   vUp = random(vmin, vmax);
   vRight = random(vmin, vmax);
   vDown = random(vmin, vmax);
   
   
   //nachfolgend werden 4 verschiedene Simulationsmuster beschrieben
   //#1 Grautöne wie auf Muster in Aufgabe
   if (selection == 1){
     if (x1 < 250  && y1 > 200 ){
           cl = int(random(110, 130));
      }
      if (x1 < 150 && (y1 > 100 && y1 < 250)){
          cl = int(random(125, 175));
      }
      if (x1 < 170  && y1 < 170 ){
            cl = int(random(180, 200));
      }
      if ((x1 < 300 && x1 > 75) && y1 < 175){
            cl = int(random(155, 175));
      }
      if ((x1 < 600 && x1 > 250) && y1 < 130){
            cl = int(random(180, 200));
      }
      if (x1 > 550 && y1 < 400){
          cl = int(random(125, 175));
      }
      if ((x1 < 650 && x1 > 200) && (y1 > 75 && y1 < 330)){
          cl = int(random(125, 175));
      }
      if (x1 > 300 && x1 < 650 && y1 > 300 && y1 < 400){
        cl = int(random(180, 200));
      }
      if (x1 > 500 && x1 < 650 && y1 > 230 && y1 < 300){
        cl = int(random(180, 200));
      }
      if (x1 > 650 && x1 < 700 && y1 > 400 && y1 < 450){
        cl = int(random(180, 200));
      }
      if (x1 > 210 && x1 < 260 && y1 > 240 && y1 < 290){
        cl = int(random(180, 200));
      }
      if (x1 > 370 && x1 < 600 && y1 > 370 && y1 < height){
        cl = int(random(130, 150));
      }
   }
   
   //#2 zufällige Verteilung
   if (selection == 2){
        cl = int(random(100, 200));
   }
   
   //#3 senkrechte Vierteilung
   if(selection == 3){
     if(x1 < width/4){
       cl = int(random(100, 125));
     }
     else if(x1 < width/2 && x1 >= width/4){
       cl = int(random(125, 150));
     }
     else if(x1 < 3*width/4 && x1 >= width/2){
       cl = int(random(150, 175));
     } else {
       cl = int(random(175, 200));
     }
   }
   
   //#4 Aufteilung in Quadranten
   if(selection == 4){
     if(x1 < width/2 && y1 < height/2){
       cl = int(random(100, 125));
     }
     else if(x1 > width/2 && y1 < height/2){
         cl = int(random(125, 150));
     }
     else if(x1 < width/2 && y1 > height/2){
         cl = int(random(150, 175));
     } else {
         cl = int(random(175, 200));
     }
   }
   
    
   //boolean, die ausdrückt, ob das Viereck gezeichnet werden darf oder nicht
   boolean valid = true;
   
   for (irrSquare p : irrSquares){
     //4 Vektoren werden erstellt
      vektoren[0] = new PVector(p.x1,p.y1);
      vektoren[1] = new PVector(p.x2,p.y2);
      vektoren[2] = new PVector(p.x3,p.y3);
      vektoren[3] = new PVector(p.x4,p.y4);
      
      boolean hit = SquarePointCollision(vektoren, x1,y1);
     //wenn das neue Viereck in einem schon bestehenden Viereck neu erscheinen will, wird dies nicht zugelassen
     if (hit){
       valid = false;
       break;
     }
   }
   
   //wenn das neue Viereck außerhalb erscheint, wird das Zeichnen genehmigt, sonst nicht
   if (valid){
       return new irrSquare(x1, y1, x2, y2, x3, y3, x4, y4, cl, vLeft, vUp, vRight, vDown);
   } else {
     return null;
   }
   
  
}

//hier wird überprüft, ob ein Viereck in einem anderen erscheint
boolean SquarePointCollision(PVector[] vektoren, float x1, float y1) {
  int next = 0;
  
  boolean collision = false;
  
  //jeder Vektor wird geprüft
  for (int current=0; current<vektoren.length; current++) {

    next = current+1;
    if (next == vektoren.length) next = 0;

    PVector vc = vektoren[current];    // c steht für "current"
    PVector vn = vektoren[next];       // n steht für "next"

    //prüfe, wie Punkt zu Vektoren liegt
    if (((vc.y >= y1 && vn.y < y1) || (vc.y < y1 && vn.y >= y1)) &&
         (x1 < (vn.x-vc.x)*(y1-vc.y) / (vn.y-vc.y)+vc.x)) {
            collision = !collision;
    }
  }
  return collision;
}

//Bei Betätigung des Buchstabens 's' wird Screenshot erstellt und bei Betätigung des Buchstabens 'p' wird die Simulation unterbrochen bzw. weiter fortgeführt
void keyPressed(){
    if(key=='s'||key=='S'){
           selectFolder("Select a folder to process: ", "folderSelected");
    }
    
    if (key == 'p' || key=='P') {
      paused = !paused;
    if (paused) {
        noLoop();
    } else {
        loop();
    }
  }
    
    
}

//Öffnen des Ordners, in welchem der Screenshot abgelegt werden soll
void folderSelected(File selection){
  if (selection == null){
    return;
  } else {
    String dir2 = selection.getPath() + "\\";
    save(dir2 + "screenshot"+num+".jpg");
    num++;
    
  }
  
}
