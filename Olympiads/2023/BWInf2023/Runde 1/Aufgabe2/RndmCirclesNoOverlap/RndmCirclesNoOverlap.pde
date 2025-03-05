Circle c;

ArrayList<Circle> circles;
color cl = color(150, 150, 150);

void setup(){
  size (640, 360);
  circles = new ArrayList<Circle>();
  circles.add(new Circle(-200, -200, cl));
  
}

void draw(){
   Circle newC = newCircle();

   
   if (newC!=null){
     circles.add(newC);
   }
   
   
  for (Circle c : circles){
    if (c.growing){
      if (c.edges()){
        c.growing = false;
    } else {
      for (Circle other : circles){
        if (c != other){
          float d = dist(c.x, c.y, other.x, other.y);
          if (d - 2 < c.r + other.r){
            c.growing = false;
            break;
            }
          }
        }
      }
    }
    c.show();
    c.grow();
  }
 
}

Circle newCircle(){
   float x = random(width);
   float y = random(height);
   int cr = int(random(100,200));
   boolean valid = true;
   
   for (Circle c : circles){
     float d = dist(x, y, c.x, c.y);
     if (d < c.r){
       valid = false;
       break;
     }
   }
   
   if (valid){
       return new Circle(x, y, cr);
   } else {
     return null;
   }
}
