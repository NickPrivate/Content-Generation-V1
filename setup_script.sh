#!/bin/bash

echo "Downloading the Llama3 model..."
ollama pull llama3

echo "Setting up environment variables..."
export OLLAMA_HOST="127.0.0.1:5000"
export OLLAMA_MODELS="$HOME/.ollama/models"

echo "Setup complete!"
