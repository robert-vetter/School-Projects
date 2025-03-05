void auslesen() {
  bvalue = analogRead(A0);        //Bodenfeuchtigkeit
  hvalue = dht.readHumidity();    //Luftfeuchtigkeit
  tvalue = dht.readTemperature(); //Temperatur
  lvalue = analogRead(A1);        //Licht
}

void write_data() {
  DynamicJsonDocument doc(96);
  JsonObject json = doc.to<JsonObject>();
  json["Boden:"] = bvalue;
  json["Licht:"] = lvalue;
  json["Feuchte:"] = hvalue;
  json["Temp:"] = tvalue;
  json["Zeit: "] = runTime;
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  serializeJsonPretty(json, dataFile);
  dataFile.print("\n");
  dataFile.close();
}
