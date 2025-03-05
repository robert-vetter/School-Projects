float a= random(255);
float b= random(255);
float c= random(255);
int[] Auto = new int[10];

void setup() {
  size(1600, 400);
  
  
  for (int i = 0; i < 10; i++) {
    Auto[i] = i * 100; 
  }
  
}

void draw() {
  background(255);
   for (int i = 0; i < 10; i++) {
    fill(a, b, c);
    ellipse(Auto[i]+20, 200, 10, 10); 
     ellipse(Auto[i]+40, 200, 10, 10);
     rect(Auto[i]+18, 180, 23,10);
     Auto[i]++;
    
  }
 
}
