
#include <Servo.h>

Servo myservo;  
int pos = 0;    
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
}
int flag = 1;
void loop() {
 if(digitalRead(0) == HIGH && flag){
    myservo.write(90);
    flag = 0;
  }
  if(digitalRead(0) == LOW){
    myservo.write(0);
    flag = 1;
    }
}
