# Introduction
This Content Generation System is the Final Project for CPSC 254  Software Development with Open Source Systems.
The project is inspired by the recent viral trend on short form social media platforms known as "brain rot" in which AI generated audio is played over background gameplay (typically Minecraft parkour).
This project aims to allow users to interact with an open-source LLM model, open-source TTS model, and open-source Rendering platform to create any kind of video you desire.


# Requirements
- Python 3.12 or greater
- Ubuntu/Debian/MacOS with apt

# Environment Setup & Installation
To setup this project, ensure that your computer matches the requirements and follow the steps to create the environment and run the program

## Step 1: Install git:
```
sudo apt install git
```
## Step 2: Clone the repository
```
git clone https://github.com/NickPrivate/Content-Generation-V1.git;
cd Content-Generation-V1
```

## Step 3: Create & Activate the Virtual Environment:
```
python3 -m venv env
source env/bin/activate
```

## Step 4: Install Required Packages:
```
pip install -r requirements.txt
```

## Step 5: Run the script to download the ML model and setup env variables:
```
chmod +x setup_script.sh
./setup_script.sh
```

## Step 6: Place your desired background video in the project's root folder and rename it to gameplay.mp4

## Step 7: Run the local API - In a new terminal enter:
```
ollama serve
```

## Step 8: Run the program with Python:
```
python3 main.py
```

## Step 9: View the results with a media player (e.g., VLC):
```
sudo apt install VLC
vlc final_result.mp4
```
Note: Ensure that you are using the second audio track to hear the TTS

## Step 10: Deactivate the Virtual Environment:
```
deactivate
```


## Technologies used
- Python3
- Ollama
- Coqui TTS
- FFmpeg-python


## Future of the Project
- Possibly turn it into a monetized webapp?
- FastAPI/React/Supabase?
- Could be something cool, stay tuned :)

