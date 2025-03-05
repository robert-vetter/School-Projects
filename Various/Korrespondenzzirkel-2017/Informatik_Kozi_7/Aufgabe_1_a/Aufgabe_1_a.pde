
float x=200;                  //Initialisierung der Variablen
float y=50;
float geschwindigkeit=0;
float gravitation=0.1;

void setup(){                 //Festlegung der Fenstergröße
  size(400, 300);
}

void draw(){                  //Festlegung verschiedener Unterprogramme
  background(255);
  bewegeBall();
  prelleBall();
  zeichneBall();
}

void bewegeBall(){              //Bewegung des Balls
  y=y+geschwindigkeit;
  geschwindigkeit=+geschwindigkeit+gravitation;
  }
  
void prelleBall(){              //Wiederhochkommen des Balls
  if(y>height){
    y=height;
    geschwindigkeit=geschwindigkeit*-0.7;
  }
}
void zeichneBall(){              //Zeichnung des Balls
 stroke(0);
 fill(175);
  ellipse(x, y, 32, 32);
  }

  
/*Ohne die if-Anweisung würde der Ball einfach nur runter ins Leere fallen.
Die if-Anweisung bewirkt, dass der Ball ab einer bestimmten Höhe mit einer Geschwindigkeit sich wieder runterbewegt.
Die Höhe die der Ball springt wird immer wieder halbiert, bis er auf dem Boden liegt.
Die Geschwindigkeit mit der der Ball runterfällt beträgt immer 0,7.*/
