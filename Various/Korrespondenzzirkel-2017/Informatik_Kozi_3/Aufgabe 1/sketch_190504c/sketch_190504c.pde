float kreisX=130;
float kreisY=130;
float kreisB=90;
float kreisH=90;
float kreisLinie=255;
float kreisFarbe=0;
float hintergrundFarbe=255;
float aenderung=0.4;

float kreisD=370;
float kreisE=370;
float kreisA=90;
float kreisC=90;
float kreisLinie1=255;
float kreisFarbe1=0;
float hintergrundFarbe1=255;
float aenderung1=0.4;

float kreisF=360;
float kreisG=130;
float kreisK=90;
float kreisL=90;
float kreisLinie2=255;
float kreisFarbe2=0;
float hintergrundFarbe2=255;
float aenderung2=0.4; 

float kreisN=130;
float kreisI=360;
float kreisJ=90;
float kreisM=90;
float kreisLinie3=255;
float kreisFarbe3=0;
float hintergrundFarbe3=255;
float aenderung3=0.4; 

void setup(){
  size(500, 500);
  frameRate(120);
}

void draw(){
  background(hintergrundFarbe);
  stroke(kreisLinie);
  fill(kreisFarbe);
  ellipse(kreisX, kreisY, kreisB, kreisH);
  ellipse(kreisD, kreisE, kreisA, kreisC);
  ellipse(kreisF, kreisG, kreisK, kreisL);
   ellipse(kreisN, kreisI, kreisJ, kreisM);
   
   kreisB=kreisB+aenderung;
  kreisH=kreisH+aenderung;
  kreisLinie=kreisLinie-aenderung;
  kreisFarbe=kreisFarbe+aenderung;
 
  kreisA=kreisA+aenderung;
  kreisC=kreisC+aenderung;
  kreisLinie1=kreisLinie1-aenderung;
  kreisFarbe1=kreisFarbe1+aenderung;
  
 
  kreisK=kreisK+aenderung;
  kreisL=kreisL+aenderung;
  kreisLinie2=kreisLinie2-aenderung;
  kreisFarbe2=kreisFarbe2+aenderung;

  kreisJ=kreisJ+aenderung;
  kreisM=kreisM+aenderung;
  kreisLinie3=kreisLinie3-aenderung;
  kreisFarbe3=kreisFarbe3+aenderung;
}
