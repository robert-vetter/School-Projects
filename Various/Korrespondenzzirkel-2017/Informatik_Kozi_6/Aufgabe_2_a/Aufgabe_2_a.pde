float a=5;
float b=3;

  

   void setup(){

  a=a+b;
  println("Vor dem Aufruf:");
  println("a: "+a+"   b: "+ b);
  println("--------- Aufruf ----------------------------");
  prozedurA (a, b);
  println("-------- Aufruf beendet --------------------");
  println("a: "+a+ "   b: "+b);
}

 




void prozedurA(float x, float y){
  println("Waehrend des Aufrufs, vor der Wertzuweisung:");
  println("a: " +a+ "   b: " +b);
  println("x: " +x+ "   y: " +y);
  x=x+y;
  y=a;
  println("Waehrend des Aufrufs, nach der Wertzuweisung:");
  println("x: " +x+ "   y: " + y);


}

/*Meine Vorüberlegungen haben sich bestätigt.
 Das Programm hat den Text und die Rechnungen genau so ausgeführt,
 wie ich es mir gedacht habe.*/
 
