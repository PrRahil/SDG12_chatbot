@echo off
echo Setting up SDG 12 Sustainability Chatbot...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment created
echo.

REM Activate virtual environment and install requirements
echo Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Check if .env file exists
if not exist .env (
    echo Creating .env file from template...
    copy .env.sample .env
    echo.
    echo ⚠️  IMPORTANT: Please edit the .env file and add your Gemini API key!
    echo    1. Get your API key from: https://makersuite.google.com/app/apikey
    echo    2. Open .env file and replace 'your_gemini_api_key_here' with your actual key
    echo.
) else (
    echo ✅ .env file already exists
)

echo.
echo 🎉 Setup complete!
echo.
echo To run the application:
echo    1. Make sure you've added your Gemini API key to the .env file
echo    2. Run: venv\Scripts\activate.bat
echo    3. Run: streamlit run app.py
echo.
echo The application will open in your web browser at http://localhost:8501
echo.
pause
