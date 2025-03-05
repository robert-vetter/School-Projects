void light(){
  if (analogRead(A2) > 90){
    digitalWrite (13, HIGH);
  }
  if (analogRead(A2) <= 90){
    digitalWrite (13, LOW);
  }
}
