
float angle = 0;

void setup(){
  size(500, 500);
}

void draw() {
  background(255);

  translate(250, 250); 
  rotate(angle); 
  fill(0);
  rect(0, -3, 250, 15); 

  angle += radians(5); 
}


/* Mit translate() kann man Formen verschieben.
 Der x-Parameter gibt die Links- / Rechtsverschiebung an,
der y-Parameter gibt die Aufwärts- / Abwärtsverschiebung an.
Mithilfe von rotate() kann man Formen drehen.
Die Koordinaten werden immer um ihre relative Position zum Ursprung gedreht. 
Positive Zahlen drehen Objekte im Uhrzeigersinn 
und negative Zahlen im Uhrzeigersinn. */
