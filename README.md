# SDG 12 Chatbot - Responsible Consumption and Production

A Streamlit-based chatbot assistant powered by Google Gemini AI that helps users make sustainable purchasing decisions and adopt responsible consumption practices.

## Features

- 🌱 Eco-friendly product recommendations
- ♻️ Waste reduction tips for household and daily life
- 🔄 Recycling and repurposing guidance
- 💬 Real-time AI-powered responses using Google Gemini
- 🎨 Clean, modern chat interface
- 🔒 Secure API key management

## Quick Setup

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
1. Copy `.env.sample` to `.env`
2. Add your Google Gemini API key to the `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application
```bash
streamlit run app.py
```

## Getting Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and paste it in your `.env` file

## Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your `GEMINI_API_KEY` in the Streamlit Cloud secrets management

### Local Network Deployment
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

## Project Structure
```
sdg12_chatbot/
├── app.py              # Main Streamlit application
├── chatbot.py          # Chatbot logic and Gemini integration
├── requirements.txt    # Python dependencies
├── .env.sample         # Sample environment file
├── .env               # Your actual environment file (not in git)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Contributing

Feel free to contribute by submitting issues or pull requests to improve the chatbot's functionality and user experience.

## License

This project is open source and available under the MIT License.
