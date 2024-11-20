#!/bin/bash

echo "Installing Ollama..."
if curl -fsSL https://ollama.com/install.sh | sh; then
    echo "Ollama installed successfully."
else
    echo "Error: Failed to install Ollama. Please check your network connection or the install script."
    exit 1
fi

echo "Downloading the Llama3 model..."
if ollama pull llama3; then
    echo "Successfully downloaded the Llama3 model."
else
    echo "Error: Failed to download the Llama3 model. Please check your internet connection or 'ollama' configuration."
    exit 1
fi

echo "Setting up environment variables..."
export OLLAMA_HOST="127.0.0.1:5000"
export OLLAMA_MODELS="$HOME/.ollama/models"

echo "Setup complete!"
