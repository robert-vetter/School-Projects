void setup() {
  Serial.begin(9600);
  pinMode(pump, OUTPUT);   //Steuersignal Relais

  pinMode( Motor1, OUTPUT );   
  pinMode( Motor2, OUTPUT );
  digitalWrite( Motor1, LOW );     
  digitalWrite( Motor2, LOW );   
  
  if (!SD.begin(chipSelect)) {
    Serial.println("SD Card error");
    return;
  }
  Serial.println("card initialized");


  
}
