#include <M5Stack.h>

void setup() {
  M5.begin();

  Serial.println("Exercise 3: ASCII Converter");
  
  M5.update();
}

int readData = 0;

void loop() {
  if (Serial.available() > 0) {
    readData = Serial.read();
    Serial.print("READ ");
    // Add your code here
    Serial.print(readData);
    
    Serial.print(" - ");
    Serial.print(", DEC: ");
    Serial.print(readData, DEC);
    
    Serial.print(", HEX: 0x");
    Serial.print(readData, HEX);
    
    Serial.print(", BIN: ");
    Serial.print(readData, BIN);
    
    Serial.println(" .. done");
  }

  M5.update();
}
