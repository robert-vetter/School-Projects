
float ypos;
float geschwindigkeit = 1;

void setup () {
  size(320, 320);
  smooth ();
  ypos = 160 ;
}
 
void draw () {
  background (255);
  if (ypos > width) {
    geschwindigkeit = geschwindigkeit * -1;
  }
  if (ypos < 2) {
    geschwindigkeit = geschwindigkeit * -1;
  }
  ypos = ypos + geschwindigkeit;
 line (0, ypos, 320, ypos);
}
