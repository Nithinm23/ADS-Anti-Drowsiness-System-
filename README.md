 Project ADS - Anti Drowsiness System
# Overview
<p align="justify">
Project ADS is an advanced real-time drowsiness detection system designed to significantly improve road safety by continuously monitoring and assessing driver alertness. Using cutting-edge computer vision techniques, the system intelligently identifies signs of driver fatigue such as yawning, eye closure, head nodding, and eye direction. Upon detecting these early indicators, ADS triggers visual alerts through LED blinks, followed by auditory beeps, to warn the driver and reduce the risk of accidents caused by drowsiness.

# Abstract
<p align="justify">
Project ADS is a real-time drowsiness detection system designed to enhance driver safety by continuously monitoring and evaluating key indicators of fatigue. By leveraging advanced computer vision algorithms, the system can detect eye movements, yawning, head nodding, and eye direction, triggering immediate alerts to warn the driver. These warnings include visual alerts (LED blinks) and auditory alerts (beeps) to ensure that the driver receives sufficient time to react, minimizing the risk of accidents due to drowsiness.

# Table of Contents
- [Demo](#Demo)
- [Components](#Comopnets)
- [Hardware](#Hardware)
- [Code Base](#Code-Base)
- [Chnologies Used](#Chnologies-Used)
- [Result](#Result)
- [Conclusion](#Conclusion)


# Demo
[Demo Video](https://github.com/user-attachments/assets/3f30bb0d-1ed4-42ee-8f16-855bc9e00457)
<p align="center"><b>Demo</b></p>

## Demo Photos

<p align="center">
  <img src="https://github.com/user-attachments/assets/dcd683c8-551a-456a-95a5-ea1468ffaa7a?width=200" alt="Screenshot 2025-04-05 105928" />
  <img src="https://github.com/user-attachments/assets/3d962934-9445-4580-9528-d630faa814aa?width=200" alt="Screenshot 2025-03-27 165806" />
  <img src="https://github.com/user-attachments/assets/712d042c-a9e0-4adb-a814-e86aa1783bbb?width=200" alt="Screenshot 2025-03-27 165746" />
  <img src="https://github.com/user-attachments/assets/fd053aca-a03b-446f-8169-64ddc56432c3?width=200" alt="Screenshot 2025-03-27 165653" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/c29f85ad-f4b9-45b6-bb2e-1227e965481b?width=200" alt="Screenshot 2025-03-27 165637" />
  <img src="https://github.com/user-attachments/assets/c414e185-de8b-4164-b3d0-05d26ead6232?width=200" alt="Screenshot 2025-03-27 165606" />
  <img src="https://github.com/user-attachments/assets/40809221-329c-4bf2-a58a-01133809ebba?width=200" alt="Screenshot 2025-04-05 110204" />
  <img src="https://github.com/user-attachments/assets/6affda22-bec6-447d-acd9-9b3463d2a5d6?width=200" alt="Screenshot 2025-04-05 110142" />
</p>


# Components
Components Already Acquired/Owned
| Component | Quantity | Description |
| :---         |     :---:      |          ---: |
| Camera Module	| 1 | 	Camera for real-time video capture | 
| LEDs |	1	| LED for visual alerts | 
| Buzzer	| 1 |	Buzzer for auditory alerts	Buzzer| 
| Arduino Nano	| 1	| Microcontroller board | 

# Hardware
Pinout Diagram

[Pin Diagram](https://github.com/user-attachments/assets/2b2fc59a-0da8-45d8-b7fb-86028eccfc35)


# Code Base
Real-Time Drowsiness Detection Code

Alert System Code (LED & Buzzer)

Eye Movement Detection Code

Yawning and Head Nodding Detection Code

# Technologies Used
1. OpenCV: Open-source computer vision library used for detecting eye closure, head nodding, and yawning.
2. Medipipe: For implementing deep learning-based models to improve the accuracy of drowsiness detection.
3. Arduino Nano: The main microcontroller used to trigger alerts based on detection.
4. LED & Buzzer: Used to provide visual and auditory feedback for the driver.


# Result
Project ADS has successfully demonstrated its ability to monitor driver alertness in real-time. Some of the key accomplishments are:
Accurate Drowsiness Detection: The system accurately detects signs of drowsiness such as eye closure, yawning, and head nodding.
Real-Time Alerts: Upon detecting fatigue, the system triggers immediate visual and auditory alerts to warn the driver.
Scalability: The system can be customized with different camera angles and alert thresholds, making it adaptable to various use cases, such as different car models and driver conditions.

# Conclusion
Project ADS provides an innovative and scalable solution to enhance road safety by detecting drowsy drivers and providing timely alerts. Using advanced computer vision algorithms, the system ensures continuous monitoring and accurate detection of fatigue, making it an essential tool in preventing accidents caused by driver drowsiness.

The successful integration of real-time monitoring, adaptive camera positioning, and proactive alerting sets ADS apart as an essential system for automotive safety, transportation, and healthcare applications. The project paves the way for further improvements in drowsiness detection technology, helping to save lives on the road.
