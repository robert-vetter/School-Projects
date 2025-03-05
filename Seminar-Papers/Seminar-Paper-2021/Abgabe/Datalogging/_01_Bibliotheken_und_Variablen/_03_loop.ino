void loop() {
  pumpe();
  runTime = millis() / 1000;
  ttimer = millis();
  Motor();
  if ((timer + interval * 1000) < ttimer) { //hier werden die Intervall-Schritte durchgeführt
    timer = millis();
    auslesen();
    write_data();  
  }
  
  
}
