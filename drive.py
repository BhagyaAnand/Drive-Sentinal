int MQ3_PIN    = A0;
int BUZZ_PIN   = 8;
int MOSFET_PIN = 6;
int THRESHOLD  = 420;
bool alarmActive = false;
bool sleepAlarm  = false;

void setup() {
  Serial.begin(9600);
  pinMode(BUZZ_PIN, OUTPUT);
  pinMode(MOSFET_PIN, OUTPUT);
  digitalWrite(MOSFET_PIN, HIGH);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n');
    msg.trim();
    if (msg == "SLEEP") {
      sleepAlarm = true;
      tone(BUZZ_PIN, 1500);
    }
    if (msg == "AWAKE") {
      sleepAlarm = false;
      if (!alarmActive) noTone(BUZZ_PIN);
    }
  }

  int alcohol = analogRead(MQ3_PIN);

  if (alcohol > THRESHOLD && !alarmActive) {
    digitalWrite(MOSFET_PIN, LOW);
    tone(BUZZ_PIN, 1000);
    Serial.println("ALCOHOL_DETECTED");
    alarmActive = true;
  }

  if (alcohol <= THRESHOLD && alarmActive) {
    digitalWrite(MOSFET_PIN, HIGH);
    if (!sleepAlarm) noTone(BUZZ_PIN);
    Serial.println("ALCOHOL_CLEAR");
    alarmActive = false;
  }

  delay(500);
}
