int[] Auto = new int[10];

void setup() {
  size(1200, 400);
  
  
  for (int i = 0; i < 10; i=i+1) {
    Auto[i] = i * 60; 
  }
}

void draw() {
  background(255);
  for (int i = 0; i < 10; i=i+1) {
    ellipse(Auto[i]+20, 200, 10, 10); 
     ellipse(Auto[i]+40, 200, 10, 10);
     rect(Auto[i]+18, 180, 23,10);
    Auto[i]++; 
    
  }
}
