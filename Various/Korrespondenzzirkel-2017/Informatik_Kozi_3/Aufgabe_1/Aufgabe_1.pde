float kreisX=250;
float kreisY=250;
float kreisA=120;
float kreisB=120;
float kreisLinie=255;
float kreisFarbe=0;
float hintergrundFarbe=255;
float aenderung=0.4;

void setup(){
  size(500, 500);
}

void draw(){
  background(hintergrundFarbe);
  stroke(kreisLinie);
  fill(kreisFarbe);
  rect(20, 20, 460, 460);
  fill(255);
  ellipse(kreisX, kreisY, kreisA, kreisB);
  
  kreisA=kreisA+aenderung;
  kreisB=kreisB+aenderung;
  kreisLinie=kreisLinie-aenderung;
  kreisFarbe=kreisFarbe+aenderung;
 
  
}
 
