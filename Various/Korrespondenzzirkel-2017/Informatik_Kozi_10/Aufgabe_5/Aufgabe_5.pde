void setup() {
  size(500, 300);
}

void draw() {
  background(255);
  stroke(0);
  noFill();
  zeichneKreis(width/2, height/2, 300);
}

void zeichneKreis(float x, float y, float radius) {
  ellipse(x, y, radius, radius);
  if (radius > 2) {
    zeichneKreis(x + radius/2, y, radius/2);
   zeichneKreis(x - radius/2, y, radius/2);
  }
}
