void pumpe(){
  if (analogRead(A0) > 400){
    digitalWrite(pump, LOW);
    }
    else{
      digitalWrite(pump, HIGH);
    }
}
