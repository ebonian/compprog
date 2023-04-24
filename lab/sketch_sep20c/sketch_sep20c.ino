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

const int note[] = {nE4, nE4, nE4, nE4, nE4, nE4, nE4, nG4, nC4, nD4, nE4, nF4, nF4, nF4, nF4, nF4, nE4, nE4, nE4, nD4, nD4, nE4, nD4, nG4};
const int duration[] = {4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 1, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 2, 1};

int i = 0;

void setup() {
  M5.begin();
  M5.update();
}

void loop() {
  if (M5.BtnA.wasPressed()) {
    M5.Speaker.tone(note[i]); 
  }

  if (M5.BtnA.wasReleased()) {
    M5.Speaker.mute();
    i++;
  }

  if (i == 24) {
    i = 0;
  }
  
  M5.update();
}
