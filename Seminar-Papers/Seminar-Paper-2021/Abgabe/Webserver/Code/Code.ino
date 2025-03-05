#include <SPI.h>
#include <Ethernet.h>
#include <SD.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

//Größe des Speichers für den HTTP-Request
#define Puffer_Anfrage   20
#define DHTPIN 4
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,178,182);   
EthernetServer server(80);       
File browser;                    
char HTTP_Anfrage[Puffer_Anfrage] = {0};  // HTTP Anfrage initialisiert als Character-Array, welcher mit einer 0 aufhört
char Anfrage_index = 0;  
boolean ZeileLeer;            

void setup()
{
    // Ethernet - Shield deaktivieren
    pinMode(10, OUTPUT);
    digitalWrite(10, HIGH);
    
    Serial.begin(9600);       
    
    // SD-Karte initialisieren
    Serial.println("Initializing SD card...");
    if (!SD.begin(4)) {
        Serial.println("ERROR - SD card initialization failed!");
        return;    
    }
    Serial.println("SUCCESS - SD card initialized.");
    if (!SD.exists("index.htm")) {
      Serial.println("ERROR - Can't find index.htm file!");  
      return;  
    }
    if (!SD.exists("datalog.txt")) {
      Serial.println("ERROR - Can't find DATALOG.htm file!");  
      return;  
    }
    if (!SD.exists("page2.htm")) {
      Serial.println("ERROR - Can't find page2.htm file!");  
      return;  
    }
    if (!SD.exists("page3.htm")) {
      Serial.println("ERROR - Can't find page3.htm file!");  
      return;  
    } 
    Serial.println("SUCCESS - All necessary files were found");
    
    Ethernet.begin(mac, ip);  
    server.begin();           
}

void loop(){
    EthernetClient client = server.available();  
    if (client) {  
        ZeileLeer = true;
        while (client.connected()) {
            if (client.available()) {   
                char ch = client.read(); 
                if (Anfrage_index < (Puffer_Anfrage - 1)) {   //Anfrage index und Puffer-Anfrage auf diesselbe Länge setzen
                    HTTP_Anfrage[Anfrage_index] = ch;          // HTTP-Anfrage speichern
                    Anfrage_index++;                          // Index um 1 erweitern
                }
                Serial.print(ch);    // HTTP_request auf seriellem Monitor ausgeben
                // letzte Zeile ist immer leer und endet mit "\n"
                // nur auf Browser antworten, wenn wirklich der ganze Request übertragen wurde (letzte Zeile leer, "\n")
                if (ch == '\n' && ZeileLeer) {
                    // Standardantwort an Browser senden
                    client.println("HTTP/1.1 200 OK");
                    client.println("Content-Type: text/html");
                    client.println("Connnection: close");
                    client.println();
                    // Gewünschte Seite wird geöfnnet
                    if (StringIncludes(HTTP_Anfrage, "GET / ") || StringIncludes(HTTP_Anfrage, "GET /index.htm")) {
                        browser = SD.open("index.htm");        // index.htm von SD-Karte öffnen
                    } else if (StringIncludes(HTTP_Anfrage, "GET /page2.htm")) {
                        client.println("Bodenfeuchtigkeit: ") ; 
                        client.print(analogRead(A0));   
                        client.println("        Licht: ");
                        client.print(analogRead(A1));         
                    } else if (StringIncludes(HTTP_Anfrage, "GET /page3.htm")) {
                        browser = SD.open("datalog.txt");       
                    }
                    if (browser) {
                        while(browser.available()) {
                            client.write(browser.read());
                        }
                        browser.close();
                    }
                    // wenn geschlossen, alle Anfragen wieder auf 0 setzen
                    Anfrage_index = 0;
                    StringLeeren(HTTP_Anfrage, Puffer_Anfrage);
                    break;
                }
                if (ch == '\n') {
                    ZeileLeer = true;
                } else if (ch != '\r') {
                    ZeileLeer = false;
                }
            } 
        } 
        delay(1);      // Webbrowser braucht kurz, um Daten zu empfangen
        client.stop(); // Verbindung zu Browser unterbrechen
    } 
}

// überprüft, ob String (der angibt, welche Seite man öffnen möchte) im HTTP-Request enthalten ist -> wenn ja, kann jeweilige Seite geöffnet werden
char StringIncludes(char *string, char *zuFinden){
    char gefunden = 0;
    char index = 0;
    if (strlen(zuFinden) > strlen(string)) {
        return 0;
    }
    while (index < strlen(string)) {
        if (string[index] == zuFinden[gefunden]) {
            gefunden++;
            if (strlen(zuFinden) == gefunden) {
                return 1;
            }
        } else {
            gefunden = 0;
        }
        index++;
    }

    return 0;
}

// Funktion, um HTTP-Anfrage zu leeren
void StringLeeren(char *string, char length){
    for (int i = 0; i < length; i++) {
        string[i] = 0;
    }
}
