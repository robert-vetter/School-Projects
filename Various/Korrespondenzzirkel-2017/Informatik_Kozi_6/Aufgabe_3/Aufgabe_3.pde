void setup(){
  
 size(800, 800);
 background(255);
}

void draw(){
  FlugzeugLinksOben();
  FlugzeugRechtsOben();
  FlugzeugInMitte();
  FlugzeugLinksUnten();
  FlugzeugRechtsUnten();
}
  
void FlugzeugLinksOben(){
   fill(0);
  rect(125, 180, 5, 40);                     //Rad 3, 4
  rect(275, 180, 5, 40);                     //Rad 1, 2
  fill(255);
  fill(0, 205, 205);
  ellipse(300, 200, 30, 30);                  //Cockpit
  fill(0, 139, 139);
  rect(100, 185, 200, 30);                    //Flugzeugrumpf
  fill(175);
  triangle(175, 185, 225, 185, 175, 20);      //Flügel oben
  triangle(175, 215, 225, 215, 175, 360);     //Flügel unten
                                       
}


void FlugzeugRechtsOben(){
   fill(255);
  rect(507, 213, 2, 10);                     //Rad 3, 4
  rect(533, 213, 2, 10);                     //Rad 1, 2
  fill(65, 2, 176);
  ellipse(540, 218, 6, 6);                  //Cockpit
  fill(76, 84, 268);
  rect(500, 215, 40, 6);                    //Flugzeugrumpf
  fill(89);
  triangle(515, 215, 525, 215, 515, 175);      //Flügel oben
  triangle(515, 221, 525, 221, 515, 255);     //Flügel unten
                                       
}

void FlugzeugInMitte(){
  fill(0, 255, 0);
  rect(433, 397, 2.5, 21);
  rect(507, 397, 2.5, 21);
  fill(255,0 ,0);
  ellipse(520, 407.5, 15, 15);
  fill(0, 0, 255);
  rect(420, 400, 100, 15);
  fill(255, 0, 255);
  triangle(455, 400, 485, 400, 455, 330);
  triangle(455, 415, 485, 415, 455, 485);
  
}

void FlugzeugLinksUnten(){
  fill(255, 255, 0);
  rect(150, 572, 6, 49.75); 
  fill(0, 255, 255);
  rect(335, 572, 6, 49.75);
  fill(255, 0, 255);
  ellipse(355, 596.875, 33.75, 33.75);
  fill(0, 0, 255);
  rect(130, 580, 225, 33.75);
  fill(0);
  triangle(202.5, 580, 282.5, 580, 202.5, 400);
  triangle(202.5, 613.75, 282.5, 613.75, 202.5, 793.75);
}

void FlugzeugRechtsUnten(){
  fill(255, 255, 0);
  rect(580, 595, 3.5, 21.25);
  rect(635, 595, 3.5, 21.25);
  fill(255, 0, 255);
  ellipse(645, 605.625, 11.25, 11.25);
  fill(255, 255, 0);
  rect(570, 600, 75, 11.25);
  fill(0, 0, 255);
  triangle(597, 600, 618, 600, 597, 535.125);
  triangle(597, 611.25, 618, 611.25, 597, 672.125);
}
