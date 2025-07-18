#!/bin/bash

echo "LinkedIn Profile Analyzer - Setup Script"
echo "=========================================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from your package manager or https://python.org"
    exit 1
fi

echo "Python found. Checking version..."
python3 --version

echo
echo "Creating virtual environment..."
python3 -m venv venv

echo
echo "Activating virtual environment..."
source venv/bin/activate

echo
echo "Upgrading pip..."
pip install --upgrade pip

echo
echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Setup completed successfully!"
echo
echo "Next steps:"
echo "1. Copy .env.example to .env"
echo "2. Fill in your API keys in the .env file"
echo "3. Run: source venv/bin/activate && python app.py"
echo
