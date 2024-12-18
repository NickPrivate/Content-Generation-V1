# Introduction
This Content Generation System is the Final Project for CPSC 254  Software Development with Open Source Systems.
The project is inspired by the recent viral trend and Oxford's word of the year, "brain rot". The most common kind of brain rot includes AI generated audio played over background gameplay (typically Minecraft parkour).
This project aims to allow users to create their OWN brainrot by using open-source LLM models, open-source TTS models, and an open-source Rendering platform to create any kind of video you desire.


## Requirements
- Python 3.12 or greater
- ~20gb of storage space
- Ubuntu/Debian/MacOS with apt. We highly recommend [Ubuntu 24.04.1 LTS ](https://ubuntu.com/download/desktop)
- Your background gameplay (must be .mp4 format & named gameplay.mp4)
- Recommend following the stps as a user account in Linux (not as root/sudo)
- Be Willing to follow all of the steps


## Environment Setup & Installation
To setup this project, ensure that your computer meets the requirements and follow the steps to create the environment and run the program

# Create the Environment

## Step 1: Update packages and Install git:
```
sudo apt update && sudo apt install -y git
```
## Step 2: Clone the repository
```
git clone https://github.com/NickPrivate/Content-Generation-V1.git
cd Content-Generation-V1
```

## Step 3: Include your background gameplay (.mp4 file)
-  Place your gameplay inside of the project's root folder and rename it to "gameplay.mp4"
-  We recommend using a Youtube to MP4 Platform like: https://cnvmp3.com/
  
## Step 4: Run the Setup Script to Download the ML Model/Requirements/Env Variables:
```
chmod +x setup_script.sh
./setup_script.sh
```

## Step 5: Source bash, and download the LLM: 
```
. ~/.bashrc
ollama pull llama3.2
```

# Running The Program

## Step 1: Create & Activate the Virtual Environment:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Step 2: Open a new terminal, Run the Ollama API:
```
ollama serve
```

## Step 3: In the original terminal, Run the program with Python:
```
python3 gui.py
```

## Step 4: View the results with a media player (e.g., VLC):
```
vlc final_result.mp4
```
Note: Ensure that you are using the second audio track to hear the TTS

## Step 5: Deactivate the Virtual Environment:
```
deactivate
```

## Troubleshooting:
- First ensure you meet the requirements: Python 3.12+, 20gb+ of storage, your own mp4 file
- If you are having errors with running the python file, follow these troubleshooting steps:
- Close all terminals, open 2 new terminals and ensure that the model is donloaded
- Do this by running the server with "ollama serve" and then in another terminal use "ollama list"
- If you do not see the model there, enter the command "ollama pull llama3.2"
- Now you should try to run the proram again, make sure to cd to the projects root directory
- Then "srouce env/bin/activate" now try running the program with "python3 gui.py"

## Technologies used
- Python3
- Pyside6
- Ollama
- llama3.2
- Coqui TTS
- FFmpeg
- espeak-ng
- VLC
