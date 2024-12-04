# Introduction
This Content Generation System is the Final Project for CPSC 254  Software Development with Open Source Systems.
The project is inspired by the recent viral trend on short form social media platforms known as "brain rot" in which AI generated audio is played over background gameplay (typically Minecraft parkour).
This project aims to allow users to interact with an open-source LLM model, open-source TTS model, and open-source Rendering platform to create any kind of video you desire.


# Requirements
- Python 3.12 or greater
- Ubuntu/Debian/MacOS with apt

# Environment Setup & Installation
To setup this project, ensure that your computer matches the requirements and follow the steps to create the environment and run the program

## Step 1: Update packages and Install git:
```
sudo apt update && sudo apt install -y git
```
## Step 2: Clone the repository
```
git clone https://github.com/NickPrivate/Content-Generation-V1.git
cd Content-Generation-V1
```

## Step 3: Install & Create & Activate the Virtual Environment:
```
python3 -m venv env
source env/bin/activate
```

## Step 4: Run the Setup Script to Download the ML Model/Requirements/Env Variables:
```
chmod +x setup_script.sh
sudo ./setup_script.sh
```

## Step 5: Include your background gameplay (.mp4 file)
-  Place your gameplay inside of the project's root folder and rename it to "gameplay.mp4"


# Running The Program

## Step 0: Ensure you are using the Python virtual environment
```
source env/bin/activate
```

## Step 1: Create a new terminal, Run the Ollama API:
```
ollama serve
```

## Step 2: In the original terminal, Run the program with Python:
```
python3 main.py
```

## Step 3: View the results with a media player (e.g., VLC):
```
vlc final_result.mp4
```
Note: Ensure that you are using the second audio track to hear the TTS

## Step 4: Deactivate the Virtual Environment:
```
deactivate
```


## Technologies used
- Python3
- Ollama
- llama3.2
- Coqui TTS
- FFmpeg
- espeak-ng

