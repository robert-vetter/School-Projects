void Motor(){
  if (dht.readTemperature() > 20) {
    digitalWrite( Motor2, HIGH );     // Drehrichtung im Uhrzeigersinn
  }
  if (dht.readTemperature() < 20) {
    digitalWrite( Motor2, LOW );    
  }
}
