void setup() {
  size(800, 800);
  background(255);
  smooth();
  noStroke();
  triangleSierpinski(0, 700, 400, 0, 800, 700, 7);
}

void triangleSierpinski(float x1, float y1, float x2, float y2, float x3, float y3, int n) {
  if ( n > 0 ) {
    fill(0, 128/n, 128);
    triangle(x1, y1, x2, y2, x3, y3);
    
    float h1 = (x1+x2)/2.0;
    float w1 = (y1+y2)/2.0;
    float h2 = (x2+x3)/2.0;
    float w2 = (y2+y3)/2.0;
    float h3 = (x3+x1)/2.0;
    float w3 = (y3+y1)/2.0;
    
    
    triangleSierpinski(x1, y1, h1, w1, h3, w3, n-1);
    triangleSierpinski(h1, w1, x2, y2, h2, w2, n-1);
    triangleSierpinski(h3, w3, h2, w2, x3, y3, n-1);
  }
}
