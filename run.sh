#!/bin/bash

echo "Starting SDG 12 Sustainability Chatbot..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found"
    echo "Please run setup.sh first"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found"
    echo "Please copy .env.sample to .env and add your Gemini API key"
    exit 1
fi

# Activate virtual environment and run the app
source venv/bin/activate
echo "✅ Virtual environment activated"
echo "🚀 Starting Streamlit application..."
echo
echo "The application will open in your web browser at http://localhost:8501"
echo "Press Ctrl+C to stop the application"
echo
streamlit run app.py
