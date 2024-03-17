@echo off
setlocal enabledelayedexpansion

REM Define the current script's path
set "script_path=%~dp0"

REM Create a Python virtual environment
python -m venv "%script_path%venv"

REM Activate the virtual environment (Windows)
call "%script_path%venv\Scripts\activate"

REM Install dependencies from the file dependences.txt using pip
pip install -r "%script_path%dependences.txt"

REM Deactivate the virtual environment
deactivate

echo "Virtual environment created and dependencies installed successfully."
pause
