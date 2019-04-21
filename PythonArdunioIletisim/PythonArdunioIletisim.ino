#include <Servo.h>
Servo kapiMotor; // yeni bi motor tanımladık
int kapiMotorPin = 7, kapiDerece=0;


const int led=13;
void setup() 
{ 
  pinMode(led, OUTPUT);
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once

 kapiDerece = 0;
  kapiMotor.attach(kapiMotorPin);  // arduinonun 8. pinini çıkış yaptık.
  kapiMotor.write(kapiDerece);  // motora ilk 0.derecesinden başlaması komutunu verdik
}
void loop() {
  char inByte = ' ';
  if(Serial.available())
  {
    char inByte = Serial.read(); // read the incoming data
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line
    if(inByte != ' ')
    {
      kapiMotor.write(90);  // motora ilk 0.derecesinden başlaması komutunu verdik
      digitalWrite(13, HIGH);
    }
    delay(5000);
    kapiMotor.write(0);  // motora ilk 0.derecesinden başlaması komutunu verdik
    digitalWrite(13, LOW);
  }
}
