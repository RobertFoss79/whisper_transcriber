Whisper Transcription Tools

Taking notes and trying to rememeber what I was typing and listen at the same time just doesn't work well. And constantly pausing to take notes resulted in a one hour lesson taking upwards of two to three hours. So, I wanted a program to transcribe the MP3 file for me. Then, I copy and paste the transcription into AI and get the notes for the lesson so I can just follow along and pay attention. This program is the result of that need for myself.

This project contains two Python scripts for transcribing audio files using OpenAI's Whisper model., written using Gemini AI.

whisper_batch.py: Automatically transcribes all MP3s in a specific "todo" folder.

whisper_transcriber.py: Transcribes a single specific file passed via command line.

Prerequisites & Setup

Crucial: Always run these scripts inside a Python virtual environment (venv).

1. Set up the Virtual Environment

Before installing anything, create and activate a clean environment:

# 1. Create the venv (run once)
python -m venv venv

# 2. Activate the venv (run every time you open a new terminal)
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


(You will see (venv) appear at the start of your command prompt line).

2. Install Dependencies

Once the (venv) is active, install the required tools:

FFmpeg: Required by Whisper to process audio. (Install via your system package manager or download from ffmpeg.org and add to PATH).

Python Libraries:

pip install openai-whisper


(Note: If you want to use your NVIDIA GPU, you may need to install the specific version of PyTorch that supports CUDA. See PyTorch.org for details).

1. Batch Transcriber (whisper_batch.py)

This is the main tool for processing multiple lessons at once. It is hardcoded to your specific desktop folders.

Configuration

The script is pre-configured with the following paths:

Source (Input): C:\Users\Rober\Desktop\todo

Destination (Output): C:\Users\Rober\Desktop\Transcribed Lessons

Model: large

How to Run

Place your .mp3 files into the todo folder.

Open your terminal or command prompt.

Ensure your venv is active (.\venv\Scripts\activate).

Run the script:

python whisper_batch.py


The script will:

Load the "Large" model (takes a moment).

Process every MP3 found in the folder.

Save the resulting text files to the Transcribed Lessons folder.

2. Single File Transcriber (whisper_transcriber.py)

Use this script if you want to transcribe just one file and specify its location manually.

How to Run

Open your terminal and activate your venv.

Run the script followed by the path to the audio file:

python whisper_transcriber.py "path\to\your\audio_file.mp3"


The script will generate a text file in the same folder as the audio file with the suffix _output.txt.

Troubleshooting

"Module not found":

You probably forgot to activate the virtual environment. Run .\venv\Scripts\activate and try again.

"FileNotFoundError":

For the batch script: Ensure the todo folder exists on your desktop.

For the single script: Ensure the path you typed is correct (use quotes if there are spaces).

Slow Transcription:

If the script says "Falling back to CPU," it means it could not find an NVIDIA GPU or CUDA is not configured. The "Large" model is very slow on a CPU.

FP16 Warnings:

The scripts are set to fp16=False to ensure stability, preventing warnings about 16-bit floating point operations on CPUs.
