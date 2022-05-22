void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  
}
void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(2) == HIGH){
    Serial.println("1");
    while (digitalRead(2) == HIGH){
      delay(1);
    }
  }
   else if (digitalRead(3) == HIGH){
    Serial.println("2");
    while (digitalRead(3) == HIGH){
      delay(1);
    }
  }
  else if (digitalRead(4) == HIGH){
    Serial.println("3");
    while (digitalRead(4) == HIGH){
      delay(1);
    }
  }
  else if (digitalRead(5) == HIGH){
    Serial.println("4");
    while (digitalRead(5) == HIGH){
      delay(1);
    }
  }
}
