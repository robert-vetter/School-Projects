int positionX=0;
int positionY=100;

void setup(){
    size(200, 200);
}

void draw(){
 background(255);
  stroke(0);
  fill(175);
  ellipse(positionX, positionY, 50, 50);
  positionX=positionX+1;
}

/*Bei dem 1. Aufruf von draw() zeichnet das Programm eine Ellipse an die Position (0,100), sodass zunächst nur die Hälfte der Ellipse zu sehen ist.
Die darauf folgende Anweisung postionX=positionX+1 ist der Startpunkt für das Nächste draw().
Beim zweiten Aufruf von draw() zeichnet das Programm daher eine Ellipse an die Position (1, 100).
Beim dritten Aufruf wird dann eine Ellipse an die Position (2, 100) gezeichnet usw..
Wenn man bei 200 angekommen ist, sieht man die Ellipse nur noch zur Hälfte und bei 225 ist sie dann endgültig verschwunden.
Weitergezeichnet wird sie aber immer noch.*/
