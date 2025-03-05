int a;
int b;
int c;
int d;
int e;
int f;
int g;
int h;
int i;
int j;
int k;
int l;
int m;
int n;
int o;
int p;

void setup(){
  size(500, 500);
  a=2;
  b=2;
  c=500;
  d=2;
  e=2;
  f=2;
  g=500;
  h=2;
  i=2;
  j=2;
  k=500;
  l=2;
  m=2;
  n=2;
  o=500;
  p=2;
}

void draw(){
  background(255);
  line(a, b, c, d);
  b=b+1;
  d=d+1;
  if(b>500){
  line(e, f, h, g);
  e=e+1;
  h=h+1;}
   if(e>500){
  line(i, j, k, l);
  j=j+1;
  l=l+1;}
  if(j>500){
  line(m, n, p, o);
  m=m+1;
  p=p+1;}

}



 
 
