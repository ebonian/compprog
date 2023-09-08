#include <M5Stack.h>

int ledPin = 21;
int ledState = LOW;

void setup() {
  M5.begin();

  pinMode(ledPin, ledState);
  digitalWrite(ledPin, ledState);

  Serial.println("Exercise 4: ASCII Converter");
  Serial.println("Please input a number.");
  
  M5.update();
}

int readData = 0;

void loop() {
  if (Serial.available() > 0) {
    readData = Serial.read();
    Serial.print("READ ");
    // Add your code here
    Serial.println(readData);

//    if (readData > 48 && readData < 57) {
//        ledState = HIGH;
//        digitalWrite(ledPin, ledState);
//    } else {
//        ledState = LOW;
//        digitalWrite(ledPin, ledState);
//    }
  }

  M5.update();
}
