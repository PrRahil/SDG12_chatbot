import streamlit as st
import time
from chatbot import SDG12Chatbot

# Page configuration
st.set_page_config(
    page_title="SDG 12 Sustainability Chatbot",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS for better UI and visibility
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        color: #4a4a4a;
        font-size: 1.1em;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .chat-container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
    }
    
    .user-message {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #2196f3;
        color: #1565c0 !important;
        box-shadow: 0 2px 5px rgba(33, 150, 243, 0.2);
        animation: slideInRight 0.3s ease-out;
    }
    
    .bot-message {
        background: linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #4caf50;
        color: #2e7d32 !important;
        box-shadow: 0 2px 5px rgba(76, 175, 80, 0.2);
        animation: slideInLeft 0.3s ease-out;
    }
    
    .user-message strong, .bot-message strong {
        color: inherit !important;
        font-weight: 600;
    }
    
    .user-message p, .bot-message p {
        color: inherit !important;
        margin: 0;
        line-height: 1.6;
    }
    
    .suggestion-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 0.75rem;
        margin: 1rem 0;
    }
    
    .suggestion-card {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border: 2px solid #ff9800;
        border-radius: 10px;
        padding: 0.75rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #e65100 !important;
        font-weight: 500;
    }
    
    .suggestion-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 152, 0, 0.3);
        border-color: #f57c00;
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #dee2e6;
        color: #495057 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .sidebar-content ul {
        color: #495057 !important;
    }
    
    .sidebar-content li {
        color: #495057 !important;
        margin: 0.5rem 0;
    }
    
    .status-success {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        color: #155724 !important;
        padding: 0.75rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        margin: 0.5rem 0;
    }
    
    .status-error {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        color: #721c24 !important;
        padding: 0.75rem;
        border-radius: 8px;
        border: 1px solid #f5c6cb;
        margin: 0.5rem 0;
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .footer {
        text-align: center;
        color: #6c757d !important;
        font-size: 0.9em;
        margin-top: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        border: 1px solid #dee2e6;
    }
    
    /* Fix for chat input */
    .stChatInput > div > div > div > div {
        background-color: #ffffff !important;
        color: #333333 !important;
    }
    
    /* Ensure all text is visible */
    .stMarkdown, .stText {
        color: inherit !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 5px rgba(76, 175, 80, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 10px rgba(76, 175, 80, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def init_chatbot():
    try:
        return SDG12Chatbot()
    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("""
        **To fix this issue:**
        
        **For Streamlit Cloud:**
        1. Go to your app settings
        2. Navigate to the 'Secrets' tab
        3. Add: `GEMINI_API_KEY = "your_api_key_here"`
        
        **For Local Development:**
        1. Create a `.env` file
        2. Add: `GEMINI_API_KEY=your_api_key_here`
        """)
        return None
    except Exception as e:
        st.error(f"Initialization Error: {str(e)}")
        return None

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:
    st.session_state.chatbot = init_chatbot()

# Header
st.markdown("<h1 class='main-header'>🌱 SDG 12 Sustainability Assistant</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI companion for Responsible Consumption and Production</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 About SDG 12")
    st.markdown("""
    <div class='sidebar-content'>
        <p><strong>Responsible Consumption and Production</strong></p>
        <p>This chatbot helps you:</p>
        <ul>
            <li>🛒 Make sustainable purchasing decisions</li>
            <li>♻️ Reduce waste in daily life</li>
            <li>🔄 Learn recycling and repurposing tips</li>
            <li>🌱 Discover eco-friendly alternatives</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("📊 Status", use_container_width=True):
            if st.session_state.chatbot and st.session_state.chatbot.is_connected():
                st.markdown("<div class='status-success'>✅ Connected to AI Assistant</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='status-error'>❌ Connection Failed</div>", unsafe_allow_html=True)

# Main chat interface
if st.session_state.chatbot is None:
    st.error("⚠️ Chatbot initialization failed. Please check your GEMINI_API_KEY in the .env file.")
    st.stop()

# Quick suggestions
if not st.session_state.messages:
    st.markdown("### 💡 Quick Suggestions")
    st.markdown("Click on any suggestion below to get started:")
    
    suggestions = st.session_state.chatbot.get_quick_suggestions()
    
    # Create suggestion grid
    cols = st.columns(2)
    for i, suggestion in enumerate(suggestions):
        col = cols[i % 2]
        with col:
            # Create custom button using markdown and session state
            suggestion_key = f"suggestion_{i}"
            if st.button(suggestion, key=suggestion_key, use_container_width=True):
                # Remove emoji and use as user input
                clean_suggestion = suggestion.split(" ", 1)[1] if " " in suggestion else suggestion
                st.session_state.messages.append({"role": "user", "content": clean_suggestion})
                st.rerun()

# Display chat messages
if st.session_state.messages:
    st.markdown("### 💬 Conversation")
    
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            st.markdown(f"""
            <div class='user-message'>
                <strong>👤 You:</strong><br>
                {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='bot-message'>
                <strong>🌱 Sustainability Assistant:</strong><br>
                {message['content']}
            </div>
            """, unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("💬 Ask me about sustainable living, eco-friendly products, waste reduction, or recycling tips..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate and display assistant response
    with st.spinner("🤔 Thinking about sustainable solutions..."):
        try:
            response = st.session_state.chatbot.get_response(
                prompt, 
                conversation_history=st.session_state.messages[:-1]  # Exclude the current message
            )
            
            # Add assistant response to session state
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Rerun to display the new messages
            st.rerun()
                
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div class='footer'>
    <p>🌍 <strong>Contributing to a more sustainable future through responsible consumption</strong> 🌍</p>
    <p>Powered by Google Gemini AI | Built with Streamlit</p>
    <p><em>Together, we can make a difference for our planet! 🌱</em></p>
</div>
""", unsafe_allow_html=True)
