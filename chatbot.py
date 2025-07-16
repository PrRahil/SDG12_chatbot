import os
import google.generativeai as genai
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SDG12Chatbot:
    def __init__(self):
        """Initialize the SDG 12 chatbot with Gemini AI."""
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-06-17')
        
        # System prompt for SDG 12 focus
        self.system_prompt = """You are an expert sustainability advisor specializing in SDG 12: Responsible Consumption and Production. Your role is to help users make sustainable purchasing decisions and adopt responsible consumption practices.

Key areas of expertise:
- Eco-friendly product recommendations
- Waste reduction strategies for households and daily life
- Recycling and repurposing guidance for common items
- Sustainable shopping practices
- Circular economy principles
- Environmental impact awareness

Guidelines:
- Provide practical, actionable advice
- Be encouraging and positive about sustainable choices
- Explain environmental benefits clearly
- Suggest specific brands or alternatives when helpful
- Keep responses concise but informative
- Ask clarifying questions when needed
- Focus on achievable changes for everyday consumers

Always maintain a helpful, knowledgeable, and encouraging tone while promoting responsible consumption and production practices."""

    def get_response(self, user_message: str, conversation_history: List[Dict] = None) -> str:
        """Generate a response using Gemini AI."""
        try:
            # Prepare the full prompt with context
            full_prompt = f"{self.system_prompt}\n\nUser: {user_message}\n\nAssistant:"
            
            # Add conversation context if available
            if conversation_history:
                context = "\n".join([
                    f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                    for msg in conversation_history[-4:]  # Last 4 messages for context
                ])
                full_prompt = f"{self.system_prompt}\n\nConversation History:\n{context}\n\nUser: {user_message}\n\nAssistant:"
            
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=800,
                    temperature=0.7,
                    top_p=0.8,
                )
            )
            
            return response.text.strip()
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request right now. Error: {str(e)}"

    def get_quick_suggestions(self) -> List[str]:
        """Return a list of quick suggestion prompts for users."""
        return [
            "🛒 How can I make my grocery shopping more sustainable?",
            "♻️ What items in my home can I repurpose instead of throwing away?",
            "🌱 Recommend eco-friendly alternatives to common household products",
            "🗑️ How can I reduce food waste in my kitchen?",
            "👕 What should I consider when buying sustainable clothing?",
            "📱 How can I responsibly dispose of old electronics?",
            "🏠 Tips for reducing plastic use in my daily life",
            "🎁 Ideas for sustainable gift-giving practices"
        ]

    def is_connected(self) -> bool:
        """Check if the chatbot can connect to Gemini API."""
        try:
            test_response = self.model.generate_content("Hello")
            return True
        except:
            return False
