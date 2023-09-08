#include <M5Stack.h>
const int nC4 = 262;
const int nD4 = 294;
const int nE4 = 330;
const int nF4 = 349;
const int nG4 = 392;
const int nA4 = 440;
const int nB4 = 494;
const int nC5 = 262 * 2;
const int nD5 = 294 * 2;
const int nE5 = 330 * 2;
const int nF5 = 349 * 2;
const int nG5 = 392 * 2;
const int nA5 = 440 * 2;
const int nB5 = 494 * 2;

const int note[] = {nD5,nC5,nD5,nF4,nC5,nA4,nA4,nA4};

void setup() {
  M5.begin();
}

void loop() {
  for (int i=0;i<8;i++) {
    int wait=1000/duration[i];
    M5.Speaker.tone(note[i]);
    delay(wait);
    M5.Speaker.mute();
    delay(50);
  }
  M5.Speaker.mute();
  delay(2000);
  M5.update();
}
