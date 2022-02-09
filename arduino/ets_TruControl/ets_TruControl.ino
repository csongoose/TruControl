//pin number declaration. Change this, if you want!
#define srl1 0                //not used yet
#define srl2 1                //not used yet
#define blinkerRight 12       //pin for left blinker
#define blinkerLeft 13        //pin for right blinker
#define highBeams 11          //pin for high beams
#define lowBeams 10           //pin for low beams
#define parkingLights 9       //pin for parking lights
#define airPressureW 8        //pin for air pressure warning light
#define batteryWarning 7      //pin for battery warning light
#define parkBrakeLt 6         //pin for parking brake (not for the light, checks the position of the lever)
#define fuelWarn 5            //pin for fuel warning lever
#define retLight 4            //pin for retarder lever
String val;

void pinIO(int pin, String expmsgonhigh, String expmsgonlow) {


  if (val == expmsgonhigh) {
    digitalWrite(pin, HIGH);
  } else if (val == expmsgonlow) {
    digitalWrite(pin, LOW);
  }
}

void setup() {

  Serial.begin(9600);
  pinMode(blinkerRight, OUTPUT);
  pinMode(blinkerLeft, OUTPUT);
  pinMode(highBeams, OUTPUT);
  pinMode(lowBeams, OUTPUT);
  pinMode(parkingLights, OUTPUT);
  pinMode(airPressureW, OUTPUT);
  pinMode(batteryWarning, OUTPUT);
  pinMode(parkBrakeLt, OUTPUT);
  pinMode(fuelWarn, OUTPUT);
  pinMode(retLight, OUTPUT);
  digitalWrite(blinkerLeft, LOW);
  digitalWrite(blinkerRight, LOW);
  digitalWrite(highBeams, LOW);
  val = "";
}

void loop() {

  
 
 if (Serial.available() > 0) {
   val = Serial.readStringUntil('\n');

  if (val == "boff") {
    digitalWrite(blinkerLeft, LOW);
    digitalWrite(blinkerRight, LOW);
  } else if (val == "lbon") {
    digitalWrite(blinkerLeft, HIGH);
    digitalWrite(blinkerRight, LOW);
  } else if (val == "rbon") {
    digitalWrite(blinkerLeft, LOW);
    digitalWrite(blinkerRight, HIGH);
  } else if (val == "hzon") {
    digitalWrite(blinkerLeft, HIGH);
    digitalWrite(blinkerRight, HIGH);
  }

  pinIO(highBeams, "hbon", "hboff");
  pinIO(lowBeams, "lowbon", "lowboff");
  pinIO(parkingLights, "plon", "ploff");
  pinIO(airPressureW, "apon", "apoff");
  pinIO(batteryWarning, "bwon", "bwoff");
  pinIO(parkBrakeLt, "pbon", "pboff");
  pinIO(fuelWarn, "fuwoff", "fuwon");
  pinIO(retLight, "reton", "retoff");
 }
}

