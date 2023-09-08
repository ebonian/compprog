#include <M5Stack.h>

int counter = 5;

void setup() {
  // put your setup code here, to run once:
  M5.begin();
  Serial.println("Hello World");
  M5.update();
  M5.Lcd.print(counter);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (M5.BtnA.wasPressed()) {
    if (counter > 0) {
      counter--;
    } else if (counter ==0) {
      M5.Speaker.tone(294);
      delay(1000);
      M5.Speaker.mute();
    }
    M5.Lcd.clearDisplay();
    M5.Lcd.setCursor(0, 0);
    M5.Lcd.print(counter);
  }
  if (M5.BtnC.wasPressed()) {
    if (counter < 10) {
      counter++;
    } else if (counter == 10) {
      M5.Speaker.tone(294);
      delay(1000);
      M5.Speaker.mute();
    }
    M5.Lcd.clearDisplay();
    M5.Lcd.setCursor(0, 0);
    M5.Lcd.print(counter);
  }
  M5.update();
}
