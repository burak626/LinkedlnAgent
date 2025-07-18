@echo off
echo LinkedIn Profile Analyzer - Setup Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Checking version...
python --version

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo.
echo Next steps:
echo 1. Copy .env.example to .env
echo 2. Fill in your API keys in the .env file
echo 3. Run: python app.py
echo.
pause
