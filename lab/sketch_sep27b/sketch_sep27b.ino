#include <M5Stack.h>

int counter = 5;

const int chars[] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"};

void printText() {
  M5.Lcd.clearDisplay();
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.setTextSize(3);

  for (int i=0;i<=10;i++) {
    if (i == counter) {
      M5.Lcd.print(chars[i]);
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  M5.begin();
  M5.Lcd.setTextSize(3);
  printText();
  M5.update();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (M5.BtnA.wasPressed()) {
    if (counter < 10) {
      counter++;
    } else if (counter == 10) {
      M5.Speaker.tone(294);
      delay(1000);
      M5.Speaker.mute();
    }
    printText();
  }
  if (M5.BtnC.wasPressed()) {
    if (counter > 0) {
      counter--;
    } else if (counter == 0) {
      M5.Speaker.tone(294);
      delay(1000);
      M5.Speaker.mute();
    }
    printText();
  }
  M5.update();
}
