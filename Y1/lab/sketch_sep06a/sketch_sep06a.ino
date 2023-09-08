#include <M5Stack.h>

int count = 0;

void setup() {
  M5.begin();
  M5.update();
}

void loop() {
  if (M5.BtnA.wasPressed()) {
    count = count + 1;
    
    Serial.print("Clicked");
    Serial.println(count);
  }
  
  M5.update();
}
