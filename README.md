# 🚗 Drive Sentinal

A real-time safety system designed to prevent accidents caused by **drunk driving** and **driver drowsiness**.

This project combines **embedded systems (Arduino)** and **computer vision** to actively monitor driver condition and take preventive action.

---

## 🔥 Features

### 🍺 Alcohol Detection System

* Detects alcohol using MQ sensor
* Triggers buzzer alert
* Gradually reduces motor/pump speed
* Displays status on LCD
* Stops system after prolonged detection

---

### 👁️ Drowsiness Detection (Computer Vision)

* Uses webcam to monitor driver's eyes
* Calculates eye openness (EAR – Eye Aspect Ratio)
* Detects eye closure in real-time
* Triggers alarm if driver is drowsy

---

## ⚙️ Tech Stack

### Hardware

* Arduino Uno
* MQ Alcohol Sensor
* 16x2 LCD with I2C module
* Buzzer
* MOSFET + Motor/Pump

### Software

* Arduino IDE (C/C++)
* Python
* OpenCV
* dlib / mediapipe

---

## 🧠 Working Principle

1. Alcohol sensor continuously checks breath alcohol level

2. If threshold exceeds:

   * Alert is triggered
   * Motor speed decreases step-by-step
   * System eventually stops

3. Camera monitors driver’s eyes

4. If eyes remain closed for a certain duration:

   * Alarm is triggered

---

## 🔌 Circuit Connections

| Component | Arduino Pin |
| --------- | ----------- |
| MQ Sensor | A0          |
| MOSFET    | D9          |
| Buzzer    | D7          |
| LCD SDA   | A4          |
| LCD SCL   | A5          |

---

## 🚀 How to Run

### Arduino Part

1. Upload the Arduino code
2. Connect all components properly
3. Power the system

### Computer Vision Part

```bash
pip install opencv-python mediapipe dlib
python drowsiness_detection.py
```

---

## 📊 Output

* LCD displays:

  * "Alcohol Detected" / "Sober"
* Buzzer alerts on unsafe condition
* Motor slows/stops
* CV system detects eye closure and alerts

---

## 🎯 Future Improvements

* GPS tracking
* SMS alert to emergency contacts
* Mobile app integration
* AI-based fatigue detection

---

## 🤝 Contributors

* Shrey Anand

---

## 📌 Project Goal

To build an **affordable and practical safety system** that reduces road accidents caused by impaired or drowsy driving.

---
