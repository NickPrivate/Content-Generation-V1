#!/bin/bash

echo "Installing required packages: python3.12-venv, vlc, espeak-ng, ffmpeg..."
sudo apt update
sudo apt install -y python3.12-venv vlc espeak-ng ffmpeg curl

if [ $? -ne 0 ]; then
    echo "Error: Failed to install required packages. Please check your network connection or package manager configuration."
    exit 1
fi

echo "Required packages installed successfully."

echo "Installing Ollama..."
if curl -fsSL https://ollama.com/install.sh | sh; then
    echo "Ollama installed successfully."
else
    echo "Error: Failed to install Ollama. Please check your network connection or the install script."
    exit 1
fi

echo "Checking if the Ollama service is running..."
if pgrep -x "ollama" > /dev/null; then
    echo "Ollama service is running."
else
    echo "Ollama service is not running. Starting it now..."
    sudo systemctl start ollama.service
    sleep 5
    if ! pgrep -x "ollama" > /dev/null; then
        echo "Failed to start the Ollama service. Exiting."
        exit 1
    fi
fi

echo "Checking network connectivity..."
if ping -c 1 google.com &> /dev/null; then
    echo "Network is reachable."
else
    echo "No network connection. Please check your internet connection and try again."
    exit 1
fi


echo "Validating and fixing the MP4 container..."
if [ -f "gameplay.mp4" ]; then
    temp_file="temp_gameplay.mp4"
    ffmpeg -i gameplay.mp4 -c copy -y "$temp_file"
    if [ $? -eq 0 ]; then
        mv "$temp_file" gameplay.mp4
        echo "MP4 container validated and fixed successfully."
    else
        echo "Error: Failed to validate/fix the MP4 container. Exiting."
        rm -f "$temp_file"
        exit 1
    fi
else
    echo "Error: gameplay.mp4 file not found. Please provide a valid MP4 file, refer to the previous step, then run this script again."
    exit 1
fi

echo "Setting up environment variables..."
export OLLAMA_HOST="127.0.0.1:5000"
export OLLAMA_MODELS="$HOME/.ollama/models"

if ! grep -q "OLLAMA_HOST" "$HOME/.bashrc"; then
    echo 'export OLLAMA_HOST="127.0.0.1:5000"' >> "$HOME/.bashrc"
    echo 'export OLLAMA_MODELS="$HOME/.ollama/models"' >> "$HOME/.bashrc"
    echo "Environment variables added to .bashrc."
fi

source ~/.bashrc

echo "Environment variables are set:"
printenv | grep OLLAMA

echo "Setup complete!"
