#!/bin/bash

# Define the current script's path
script_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create a Python virtual environment
python3 -m venv "$script_path/venv"

# Activate the virtual environment (Linux/Unix)
source "$script_path/venv/bin/activate"

# Install dependencies from the file dependences.txt using pip
pip install -r "$script_path/dependences.txt"

# Deactivate the virtual environment
deactivate

echo "Virtual environment created and dependencies installed successfully."
