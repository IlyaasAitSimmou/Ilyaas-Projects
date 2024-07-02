int EnA = 11;
int in1 = 13;
int in2 = 12;
int EnB = 3;
int in3 = 2;
int in4 = 4;
int Trig = 8;
int Echo = 9;
int Speed = 255;
int duration;
int distance;
int DuR;
int DuL;
int DiR;
int DiL;


void setup() {
  // put your setup code here, to run once:
pinMode(EnA, OUTPUT);
pinMode(in1, OUTPUT);
pinMode(in2, OUTPUT);
pinMode(EnB, OUTPUT);
pinMode(in3, OUTPUT);
pinMode(in4, OUTPUT);
pinMode(Trig, OUTPUT);
pinMode(Echo, INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

analogWrite(EnA, 255);
analogWrite(EnB, 255);

digitalWrite(Trig, LOW);
delay(2);
digitalWrite(Trig, HIGH);
delay(10);
digitalWrite(Trig, LOW);
duration = pulseIn(Echo, HIGH);
distance = duration/2*0.0343;


Serial.println(distance);
if (distance <= 30 and distance > 0) {
  Serial.println(false);
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(700);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(700);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  digitalWrite(Trig, LOW);
  delay(2);
  digitalWrite(Trig, HIGH);
  delay(10);
  digitalWrite(Trig, LOW);
  DuR = pulseIn(Echo, HIGH);
  DiR = DuR/2*0.0343;
  

  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  delay(1400);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(Trig, LOW);
  delay(2);
  digitalWrite(Trig, HIGH);
  delay(10);
  digitalWrite(Trig, LOW);
  DuL = pulseIn(Echo, HIGH);
  DiL = DuR/2*0.0343;

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  delay(700);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  if (DuR >= 30 and DuR >= DuL) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    delay(1050);
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  } else if (DuL >= 30) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    delay(1050);
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }
} else {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  Serial.println(true);
  }



}

