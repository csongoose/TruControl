#define srl1 0
#define srl2 1
#define blinkerRight 13
#define blinkerLeft 12
#define highBeams 11
int val;
int hb;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(blinkerRight, OUTPUT);
  pinMode(blinkerLeft, OUTPUT);
  pinMode(highBeams, OUTPUT);
  digitalWrite(blinkerLeft, LOW);
  digitalWrite(blinkerRight, LOW);
  digitalWrite(highBeams, LOW);
  val = 100;
  hb = 98;
}

void loop() {
  // put your main code here, to run repeatedly:
 if (Serial.available() > 0) {
   val = Serial.read();
  
  if (val == 100) {
    digitalWrite(blinkerLeft, LOW);
    digitalWrite(blinkerRight, LOW);
  } else if (val == 101) {
    digitalWrite(blinkerLeft, HIGH);
    digitalWrite(blinkerRight, LOW);
  } else if (val == 102) {
    digitalWrite(blinkerLeft, LOW);
    digitalWrite(blinkerRight, HIGH);
  } else if (val == 103) {
    digitalWrite(blinkerLeft, HIGH);
    digitalWrite(blinkerRight, HIGH);
  }
 }
}
