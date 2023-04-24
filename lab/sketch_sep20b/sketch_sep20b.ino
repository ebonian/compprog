#include <M5Stack.h>

const int nC4 = 262;
const int nD4 = 294;
const int nE4 = 330;
const int nF4 = 349;
const int nG4 = 392;
const int nA4 = 440;
const int nB4 = 494;

const int keys[] = {'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C', 'D', 'E', 'F', 'G', 'A', 'b'};
const int notes[] = {nC4, nD4, nE4, nF4, nG4, nA4, nB4, nC4 * 2, nD4 * 2, nE4 * 2, nF4 * 2, nG4 * 2, nA4 * 2, nB4 * 2};

void setup() {
  // put your setup code here, to run once:
  M5.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int key = Serial.read();
    Serial.write(key);

    for (int i=0;i<14;i++) {
      if (key == keys[i]) {
        M5.Speaker.tone(notes[i]);
        delay(1000);
        M5.Speaker.mute();
        break;
      }
    }
    delay(1300);
    menu();
  }
  M5.update();
}

void menu() {
  Serial.println("\nExercise 3\nPlease enter note [c..a, C..A]");
  Serial.print("> ");
}
