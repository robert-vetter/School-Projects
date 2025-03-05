int l = 300;

void setup() {
  size(400, 400);
  background(0);
  stroke(255);
  translate((width-l)/2, height/1.4);
  for (int i = 1; i <= 3; i++) {
    kcurve(0, l);
    rotate(radians(120));
    translate(-l, 0);
  }
}

void kcurve(float x1, float x2) {
  float s = (x2-x1)/3;
  if (s < 5) {
    pushMatrix();
    translate(x1, 0);
    line(0, 0, s, 0);
    line(2*s, 0, 3*s, 0);
    translate(s, 0);
    rotate(radians(60));
    line(0, 0, s, 0);
    translate(s, 0);
    rotate(radians(-120));
    line(0, 0, s, 0);
    popMatrix();
    return;
  }
  pushMatrix();
  translate(x1, 0);
  kcurve(0, s);
  kcurve(2*s, 3*s);
  translate(s, 0);
  rotate(radians(60));
  kcurve(0, s);
  translate(s, 0);
  rotate(radians(-120));
  kcurve(0, s);
  popMatrix();
}
