# Audio Transcription App

This project is a simple web application for transcribing audio files to text using the OpenAI Whisper model. The app is built with Python, Gradio, and Hugging Face Transformers.

## Features
- Upload audio files and get transcriptions instantly
- Uses OpenAI Whisper (tiny.en) for speech recognition
- User-friendly web interface powered by Gradio

## Requirements
- Python 3.8+
- pip (Python package manager)
- ffmpeg (audio processing tool, must be installed on your system)
- The following Python packages:
  - torch
  - transformers
  - gradio

## Installation
1. Clone this repository or download the source code.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv my_env
   source my_env/bin/activate
   ```
3. Install ffmpeg:
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - On Windows: Download from https://ffmpeg.org/download.html and add to PATH
4. Install dependencies:
   ```bash
   pip install torch transformers gradio
   ```

## Usage
Run the main app:
```bash
python speech2text_app.py
```
The Gradio web interface will launch at http://localhost:7860 (or your specified port).

## File Structure
- `speech2text_app.py`: Main application file
- `download.py`, `simple_speech2text.py`: Additional scripts (not required for main app)
- `downloaded_audio.mp3`: Example audio file
- `my_env/`: (Optional) Python virtual environment

## How It Works
- Upload an audio file via the web interface
- The app uses Hugging Face's pipeline with OpenAI Whisper to transcribe speech to text
- The transcription is displayed in the browser

## Notes
- For best results, use clear audio files in English
- The Whisper tiny model is lightweight but may be less accurate than larger models

## License
This project is for educational purposes.
# Audio-Transcription-App
