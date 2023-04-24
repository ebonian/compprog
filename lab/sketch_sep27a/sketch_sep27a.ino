#include <M5Stack.h>

int ledPin = 21;

void setup() {
  // put your setup code here, to run once:
  M5.begin();
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  M5.update();
}

int readData;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    readData = Serial.read();
    Serial.print(readData);

    if (readData >= 48 && readData <= 57) {
      M5.Speaker.tone(262);
      delay(1000);
      M5.Speaker.mute();
    } else if (readData != 10) {
      digitalWrite(ledPin, HIGH);
      delay(1000);
      digitalWrite(ledPin, LOW);
    }
  }

  M5.update();
}
