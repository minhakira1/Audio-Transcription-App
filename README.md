# Audio Transcription & Key Point Extraction App

This project is a web application for transcribing audio files to text and extracting key points using OpenAI Whisper and BART (facebook/bart-large-cnn). The app is built with Python, Gradio, and Hugging Face Transformers.

## Features
- Upload audio files and get transcriptions instantly
- Uses OpenAI Whisper (tiny.en) for speech recognition
- Extracts key points from transcripts using BART (facebook/bart-large-cnn)
- User-friendly web interface powered by Gradio

## Requirements
- Python 3.8+
- pip (Python package manager)
- ffmpeg (audio processing tool, must be installed on your system)
- The following Python packages (see requirements.txt):
  - torch
  - transformers
  - gradio
  - python-dotenv

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
   pip install -r requirements.txt
   ```

## Usage
Run the main app:
```bash
python3 speech_analyzer.py
```
The Gradio web interface will launch at http://localhost:7860 (or your specified port).

## File Structure
- `speech_analyzer.py`: Main application file
- `downloaded_audio.mp3`: Example audio file
- `flagged/`: Gradio flagged data

## Notes
- Ensure ffmpeg is installed and available in your system PATH.
- No Hugging Face token or license acceptance is required for the models used.
- The app is free to use and runs locally.

## License
This project is for educational purposes.

