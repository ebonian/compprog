#include <M5Stack.h>
#include <SimpleDHT.h>
#include <Wire.h>
#define DHTPIN 5

SimpleDHT11 dht;
int temperature, humidity;
int old_t = -1000;
int isCelcius = 0;


void setup(){
  M5.begin();
  Wire.begin();
  M5.Lcd.setTextSize(10);
}

void loop() {
  float temp,humid;

  
  int status = dht.read2(DHTPIN, &temp, &humid, NULL);
  if (status == SimpleDHTErrSuccess) {
    temperature = temp;
    humidity = humid;
  }
  
  if (M5.BtnA.wasPressed()) {
    isCelcius = isCelcius + 1;
    M5.Lcd.fillScreen(0);
    M5.Lcd.setCursor(0,0);
    if (isCelcius % 2 == 0) {
      M5.Lcd.print(temperature);
      M5.Lcd.print(" C\n");
      M5.Lcd.print(humidity);
      M5.Lcd.print(" %");
    } else {
      M5.Lcd.print(temperature * 9/5 + 32);
      M5.Lcd.print(" F\n");
      M5.Lcd.print(humidity);
      M5.Lcd.print(" %");
    }
  }
  
  if (temperature != old_t){
    if (temp > 27){
      M5.Lcd.setTextColor(0xe8e4);
    }
    else {
    M5.Lcd.setTextColor(0x2589);
    }
    M5.Lcd.fillScreen(0);
    M5.Lcd.setCursor(0,0);
    if (isCelcius % 2 == 0) {
      M5.Lcd.print(temperature);
      M5.Lcd.print(" C\n");
    } else {
      M5.Lcd.print(temperature * 9/5 + 32);
      M5.Lcd.print(" F\n");
    }

    M5.Lcd.print(humidity);
    M5.Lcd.print(" %");
  }

  old_t = temperature;
  M5.update();
}
