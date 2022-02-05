int button = 7;
int lastButtonState;
int currentButtonState;
void setup() {
  // put your setup code here, to run once:
  pinMode(button, INPUT);
  digitalWrite(button, HIGH); //activate arduino internal pull up
  Serial.begin(9600);
}
void loop() {
  delay(500);
  lastButtonState = currentButtonState;
  currentButtonState = digitalRead(button);
    if (lastButtonState == HIGH && currentButtonState == LOW){
      Serial.println("Active");  
    }
    else if (lastButtonState == LOW && currentButtonState == HIGH){
      Serial.println("Inactive");
    } 
      
    

}
