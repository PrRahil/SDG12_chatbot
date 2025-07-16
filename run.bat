@echo off
echo Starting SDG 12 Sustainability Chatbot...
echo.

REM Check if virtual environment exists
if not exist venv\ (
    echo Error: Virtual environment not found
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo Error: .env file not found
    echo Please copy .env.sample to .env and add your Gemini API key
    pause
    exit /b 1
)

REM Activate virtual environment and run the app
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo 🚀 Starting Streamlit application...
echo.
echo The application will open in your web browser at http://localhost:8501
echo Press Ctrl+C to stop the application
echo.
streamlit run app.py
