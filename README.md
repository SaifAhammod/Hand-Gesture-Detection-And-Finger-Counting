# Hand Gesture Detection and Finger Counting

This repository contains a project that uses **MediaPipe** and **OpenCV** for real-time **hand gesture detection** and **finger counting**. The system detects hand landmarks and counts the number of extended fingers in real-time using a webcam.

## Features
- **Real-Time Hand Gesture Detection**: Detects and tracks the position of hands using **MediaPipe**.
- **Finger Counting**: Counts the number of extended fingers in each detected hand using custom logic.
- **Multi-Hand Detection**: Supports detecting and counting fingers for both hands simultaneously.
- **Cross-Platform**: Works on all platforms supporting Python (Windows, macOS, Linux).

## How it Works
1. **Hand Detection**: The system uses **MediaPipe's Hand Module** to detect hand landmarks and gestures in real-time.
2. **Finger Counting**: Based on the position of the hand landmarks, the program determines which fingers are extended and counts them.
3. **Display Results**: The number of extended fingers is shown on the video feed in real-time.

## Requirements
To run the project, you need the following Python libraries:

- **OpenCV**: For capturing video from the webcam and displaying results.
- **MediaPipe**: For hand gesture detection and landmarks recognition.

Install the necessary dependencies by running:

```bash
pip install opencv-python mediapipe
