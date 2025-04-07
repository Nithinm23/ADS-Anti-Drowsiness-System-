# Project ADS - Anti Drowsiness System
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
https://github.com/user-attachments/assets/6c1867ad-4aa2-4288-a316-79d15c68843c

<p align="center"><b>Demo</b></p>

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

![Screenshot 2025-04-01 185259](https://github.com/user-attachments/assets/2b2fc59a-0da8-45d8-b7fb-86028eccfc35)


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
