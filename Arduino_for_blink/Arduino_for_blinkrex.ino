const int eogPin = A1;
int baseline = 512;
int threshold = 250;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int val = analogRead(eogPin);
  int delta = val - baseline;

  if (abs(delta) > threshold) {
    Serial.println("BLINK");
    delay(300);  // 抖动过滤
  } else {
    Serial.println("0");
  }
}
