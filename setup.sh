#!/bin/bash

echo "Setting up SDG 12 Sustainability Chatbot..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

echo "✅ Python found"
echo

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "✅ Virtual environment created"
echo

# Activate virtual environment and install requirements
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install requirements"
    exit 1
fi

echo "✅ Dependencies installed"
echo

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.sample .env
    echo
    echo "⚠️  IMPORTANT: Please edit the .env file and add your Gemini API key!"
    echo "   1. Get your API key from: https://makersuite.google.com/app/apikey"
    echo "   2. Open .env file and replace 'your_gemini_api_key_here' with your actual key"
    echo
else
    echo "✅ .env file already exists"
fi

echo
echo "🎉 Setup complete!"
echo
echo "To run the application:"
echo "   1. Make sure you've added your Gemini API key to the .env file"
echo "   2. Run: source venv/bin/activate"
echo "   3. Run: streamlit run app.py"
echo
echo "The application will open in your web browser at http://localhost:8501"
echo
