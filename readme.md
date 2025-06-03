# 🎙️ Persian Speech-to-Text Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.2-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

A web application that converts Persian (Farsi) speech in WAV audio files to text using Google's Speech Recognition API.

![Application Screenshot](demo.png) <!-- Add your screenshot here -->

## ✨ Features
- Persian/Farsi speech recognition
- Simple web interface with Streamlit
- Audio playback before processing
- Text export functionality
- Right-to-Left (RTL) text display
- Real-time processing status

## 🛠️ Technical Stack
- **Frontend**: Streamlit
- **Speech Recognition**: `speech_recognition` library
- **Audio Processing**: Temporary WAV file handling
- **Language Support**: Persian (`fa-IR`)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Chrome/Firefox (for best RTL support)

### Installation
1. Clone the repository (if available)
2. Install requirements:
```bash
    pip install streamlit SpeechRecognition
```