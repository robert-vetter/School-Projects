int Summand1=128/2;     //Hier ersten lösbaren Bruch eingeben als ersten Summand.
int Summand2=28/4;      //Hier ersten lösbaren Bruch eingeben als zweiten Summand.
int Minuend=361/19;     //Hier ersten lösbaren Bruch eingeben als Minuend.
int Subtrahend=424/4;   //Hier ersten lösbaren Bruch eingeben als Subtrahend.
int Faktor1= 52/26;     //Hier ersten lösbaren Bruch eingeben als ersten Faktor.
int Faktor2= 14/2;      //Hier zweiten lösbaren Bruch eingeben als zweiten Faktor.
int Dividend=48/6;      //Hier ersten lösbaren Bruch eingeben als Dividenden.
int Divisor=8/4;        //Hier ersten lösbaren Bruch eingeben als Divisor.
int zahl;

 
  
 void setup(){
   Addition(zahl);
   Subtraktion(zahl);
   Multiplikation(zahl);
   Division(zahl); 
   
}

void Addition(int Summe){
   println("Summand 1: " + Summand1);
    println("Summand 2: "+ Summand2);
    Summe=Summand1+Summand2;
  println("Summe: "+ Summe);
  println("");
}
  void Subtraktion(int Differenz){
   println("Minuend: " + Minuend);
    println("Subtrahend: "+ Subtrahend);
    Differenz=Minuend-Subtrahend;
  println("Differenz: "+ Differenz);
  println("");
}


  void Multiplikation(int Produkt){
  println("Faktor 1: " + Faktor1);
    println("Faktor 2: "+ Faktor2);
    Produkt=Faktor1*Faktor2;
  println("Produkt: "+ Produkt);
  println("");
}

void Division(int Quotient){
  println("Dividend: "+ Dividend);
  println("Divisor: "+ Divisor);
  Quotient=Dividend/Divisor;
  println("Quotient: "+ Quotient);
   println("");
}
  
