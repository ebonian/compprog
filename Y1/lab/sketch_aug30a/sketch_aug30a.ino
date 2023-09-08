#include <M5Stack.h>

int ledPin = 21;
int ledState = LOW;

void setup() {
  M5.begin();
  pinMode(ledPin, ledState);
  digitalWrite(ledPin, ledState);
  M5.update();
}

void loop() {
  if (M5.BtnA.wasPressed()) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  };
  if (M5.BtnB.wasPressed()) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  };
  if (M5.BtnC.wasPressed()) {
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  };
  M5.update();
}
