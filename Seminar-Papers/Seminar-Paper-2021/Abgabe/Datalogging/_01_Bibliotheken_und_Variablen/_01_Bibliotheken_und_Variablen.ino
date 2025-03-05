#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <SPI.h>
#include <SD.h>
#include <ArduinoJson.h>

#define DHTPIN 4
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);   // DHT-Bibliothek initialisieren
#define Motor1 8         // Motor Anschluss 1
#define Motor2 9             // Motor Anschluss 2  

const int chipSelect = 4;

int interval = 10;  //jede 10s Wert auf SD-Karte speichern
int pump = 3;       //Pumpe an PIN 3

long ttimer;
long timer;
String bvalue;    //Bodenfeuchtigkeit
String tvalue;    //Temperatur
String hvalue;    //Luftfeuchtigkeit
String lvalue;    //Lichtintensität
String dataString;
String runTime;
