void setup(){
  println("a");
  prozedur1();
  println("b");
}

void draw(){
  println("c");
  prozedur2();
  println("d");
  prozedur1();
  noLoop();
}

void prozedur1(){
  println("e");
  println("f");
}

void prozedur2(){
  println("g");
  prozedur1();
  println("h");
}

/*Meine Vermutung hat sich bestätigt.
 Ich habe mir gedacht, dass durch die ganzen "println" die Variablen unten in
 dem Ausgabefenster angezeigt werden. Eine offene Frage wäre z.B. warum man bei den
 Hauptfunktionen in "void setup" prozedur1(); hineingeschrieben hat.
 Normalerweise brauch man die nur in draw() reinschreiben, damit die erstmal
 "deklariert" ist. Eine weitere Frage wäre auch, warum man "println" schreibt und
 nicht einfach "print". Die Funktion "noLoop()" schreibt man in setup() hinein und es verhindert
 die kontinuierliche Ausführung in draw(). Daher könnte man fast schon sagen, dass man void draw()
 in void setup() umgewandelt hat.*/
