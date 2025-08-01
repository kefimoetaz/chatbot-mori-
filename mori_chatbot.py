"""
Mori Buntarou Mountain Chatbot
A solitary climber's wisdom through local LLM
"""

import streamlit as st
import ollama
import json
import re
import os
import base64
from typing import List, Dict
from mori_persona import MORI_SYSTEM_PROMPT, MORI_CONVERSATION_STARTERS, MORI_RESPONSE_PATTERNS
from mountain_knowledge import get_mountain_knowledge, MOUNTAIN_DATA

class MoriChatbot:
    def __init__(self, model_name: str = "llama3.2:1b"):
        self.model_name = model_name
        self.conversation_history = []
        self.mountain_knowledge = MOUNTAIN_DATA
        
    def initialize_session(self):
        """Initialize Streamlit session state"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
    def search_mountain_knowledge(self, query: str) -> str:
        """Search through mountain knowledge base"""
        query_lower = query.lower()
        relevant_info = []
        
        # Search through different categories
        for category, data in self.mountain_knowledge.items():
            if isinstance(data, dict):
                for subcategory, info in data.items():
                    if any(keyword in query_lower for keyword in [category, subcategory]):
                        if isinstance(info, dict):
                            relevant_info.append(f"{subcategory}: {info}")
                        else:
                            relevant_info.append(f"{subcategory}: {info}")
        
        return "\n".join(relevant_info[:3]) if relevant_info else ""
    
    def generate_mori_response(self, user_message: str) -> str:
        """Generate response in Mori's voice using Ollama - optimized for speed"""
        try:
            # Simplified prompt for faster response
            simple_prompt = f"""You are Mori Buntarou, a stoic mountain climber. Respond briefly and authentically.

User: {user_message}

Respond in 1-2 short sentences. Be direct, honest, sometimes distant. Don't be overly helpful."""
            
            # Call Ollama with minimal context for speed
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": simple_prompt},
                    {"role": "user", "content": user_message}
                ],
                options={
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "num_predict": 50  # Limit response length for speed
                }
            )
            
            return response['message']['content']
            
        except Exception as e:
            return "..."
    
    def apply_mori_filter(self, response: str) -> str:
        """Apply Mori's speaking patterns to the response"""
        # Remove overly enthusiastic language
        response = re.sub(r'!+', '.', response)
        response = re.sub(r'exciting|amazing|awesome|fantastic', 'significant', response, flags=re.IGNORECASE)
        
        # Keep responses clean and authentic - no repetitive additions
        return response

def get_base64_image(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def main():
    # Page configuration
    st.set_page_config(
        page_title="Mori Buntarou - Mountain Sage",
        page_icon="🏔️",
        layout="wide"
    )
    
    # Load background image
    bg_image = get_base64_image("bg.jpeg")
    
    # Enhanced CSS for immersive mountain and ice aesthetic
    bg_style = ""
    if bg_image:
        bg_style = f"background-image: linear-gradient(rgba(10, 20, 30, 0.4), rgba(20, 30, 40, 0.6)), url(data:image/jpeg;base64,{bg_image});"
    else:
        bg_style = "background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 100%);"
    
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700&family=Roboto:wght@300;400;500&display=swap');
    
    /* Modern Manga Panel Background */
    .main {{
        {bg_style}
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        position: relative;
        border: 4px solid #000;
        background-color: #FFFFFF;
    }}
    
    .stApp {{
        background: transparent;
    }}
    
    /* Clean panel overlay */
    .main::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.85);
        pointer-events: none;
        z-index: 0;
    }}
    
    /* Mori's Speech Bubble - Clean Modern */
    .stChatMessage[data-testid="chat-message-assistant"] {{
        background: #FFFFFF;
        border: 2px solid #000;
        border-radius: 20px;
        padding: 20px 25px;
        margin: 25px 20px 25px 60px;
        position: relative;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        max-width: 75%;
    }}
    
    /* Clean speech bubble tail */
    .stChatMessage[data-testid="chat-message-assistant"]::before {{
        content: '';
        position: absolute;
        bottom: -10px;
        left: 40px;
        width: 0;
        height: 0;
        border-left: 15px solid transparent;
        border-right: 15px solid transparent;
        border-top: 15px solid #FFFFFF;
    }}
    
    .stChatMessage[data-testid="chat-message-assistant"]::after {{
        content: '';
        position: absolute;
        bottom: -12px;
        left: 38px;
        width: 0;
        height: 0;
        border-left: 17px solid transparent;
        border-right: 17px solid transparent;
        border-top: 17px solid #000;
        z-index: -1;
    }}
    
    /* User Speech Bubble - Clean Modern */
    .stChatMessage[data-testid="chat-message-user"] {{
        background: #F8F9FA;
        border: 2px solid #000;
        border-radius: 20px;
        padding: 18px 22px;
        margin: 25px 60px 25px 20px;
        position: relative;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        max-width: 70%;
        margin-left: auto;
    }}
    
    /* User speech bubble tail */
    .stChatMessage[data-testid="chat-message-user"]::before {{
        content: '';
        position: absolute;
        bottom: -10px;
        right: 40px;
        width: 0;
        height: 0;
        border-left: 15px solid transparent;
        border-right: 15px solid transparent;
        border-top: 15px solid #F8F9FA;
    }}
    
    .stChatMessage[data-testid="chat-message-user"]::after {{
        content: '';
        position: absolute;
        bottom: -12px;
        right: 38px;
        width: 0;
        height: 0;
        border-left: 17px solid transparent;
        border-right: 17px solid transparent;
        border-top: 17px solid #000;
        z-index: -1;
    }}
    
    /* Modern Manga Text */
    .stChatMessage[data-testid="chat-message-assistant"] p {{
        color: #000;
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 400;
        font-size: 16px;
        line-height: 1.6;
        margin: 0;
        letter-spacing: 0.3px;
    }}
    
    .stChatMessage[data-testid="chat-message-user"] p {{
        color: #000;
        font-family: 'Roboto', sans-serif;
        font-weight: 400;
        font-size: 15px;
        line-height: 1.5;
        margin: 0;
    }}
    
    /* Clean Modern Title */
    .title {{
        color: #000;
        text-align: center;
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin: 30px 0 10px 0;
        text-shadow: none;
    }}
    
    .subtitle {{
        color: #666;
        text-align: center;
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 1.2rem;
        font-weight: 300;
        letter-spacing: 1px;
        margin: 0 0 20px 0;
        font-style: italic;
    }}
    
    /* Clean Sidebar */
    .css-1d391kg, [data-testid="stSidebar"] {{
        background: #FFFFFF;
        border-right: 3px solid #000;
        border-left: none;
    }}
    
    .css-1d391kg .markdown-text-container {{
        color: #000 !important;
        font-family: 'Roboto', sans-serif;
        font-weight: 400;
    }}
    
    /* Sidebar text styling */
    [data-testid="stSidebar"] .markdown-text-container {{
        color: #000 !important;
    }}
    
    [data-testid="stSidebar"] h3 {{
        color: #000 !important;
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 700;
    }}
    
    [data-testid="stSidebar"] p {{
        color: #000 !important;
        font-family: 'Roboto', sans-serif;
    }}
    
    [data-testid="stSidebar"] ul {{
        color: #000 !important;
    }}
    
    [data-testid="stSidebar"] li {{
        color: #000 !important;
    }}
    
    /* Modern Input */
    .stTextInput > div > div > input, .stChatInput > div > div > input {{
        background: #FFFFFF;
        color: #000;
        border: 2px solid #000;
        border-radius: 25px;
        font-family: 'Roboto', sans-serif;
        font-size: 16px;
        font-weight: 400;
        padding: 12px 20px;
        box-shadow: none;
    }}
    
    .stTextInput > div > div > input:focus, .stChatInput > div > div > input:focus {{
        border-color: #333;
        box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
        outline: none;
    }}
    
    /* Clean Button */
    .stButton > button {{
        background: #000;
        color: #FFFFFF !important;
        border: 2px solid #000;
        border-radius: 8px;
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
        font-weight: 500;
        padding: 8px 16px;
        text-shadow: none;
        box-shadow: none;
        transition: all 0.2s ease;
    }}
    
    .stButton > button:hover {{
        background: #333;
        border-color: #333;
        color: #FFFFFF !important;
        transform: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}
    
    /* Clean Selectbox */
    .stSelectbox > div > div {{
        background: #FFFFFF;
        border: 2px solid #000;
        border-radius: 8px;
        color: #000;
        font-family: 'Roboto', sans-serif;
        font-weight: 400;
        box-shadow: none;
    }}
    
    /* Character Portrait - Clean Circle */
    .logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 25px;
        background: #FFFFFF;
        border: 3px solid #000;
        border-radius: 50%;
        margin: 40px auto;
        width: 180px;
        height: 180px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
    }}
    
    /* Clean Spinner */
    .stSpinner > div {{
        border: 3px solid #E0E0E0;
        border-top: 3px solid #000;
        border-radius: 50%;
    }}
    
    /* Quote styling - Clean */
    .mountain-quote {{
        text-align: center;
        color: #666;
        background: transparent;
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        font-style: italic;
        margin: 20px auto 40px auto;
        padding: 0;
        border: none;
        max-width: 500px;
        box-shadow: none;
        position: relative;
    }}
    
    .mountain-quote::before,
    .mountain-quote::after {{
        content: '';
    }}
    
    /* Panel grid lines for manga effect */
    .panel-grid {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            linear-gradient(to right, rgba(0,0,0,0.05) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0,0,0,0.05) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 1;
        opacity: 0.3;
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Header with centered logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Center the logo
        st.markdown('<div style="display: flex; justify-content: center; margin: 20px 0;">', unsafe_allow_html=True)
        try:
            st.image("logo.png", width=600)
        except:
            pass  # No fallback emoji
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<h1 class='title'>Mori Buntarou</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='subtitle'>The Solitary Climber's </h3>", unsafe_allow_html=True)
        st.markdown("<div class='mountain-quote'>\"In silence, the mountain speaks\"</div>", unsafe_allow_html=True)
    
    # Initialize chatbot
    chatbot = MoriChatbot()
    chatbot.initialize_session()
    
    # Sidebar with mountain knowledge categories
    with st.sidebar:
      
        st.markdown("*Ask Mori about:*")
        st.markdown("- Climbing techniques")
        st.markdown("- Mountain weather")
        st.markdown("- Equipment and gear")
        st.markdown("- Famous peaks")
        st.markdown("- Japanese mountains")
        st.markdown("- Hazards and safety")
        
        st.markdown("---")
        st.markdown("### ⚙️ Settings")
        model_choice = st.selectbox(
            "Ollama Model",
            ["llama3.2:1b", "mistral", "llama3", "phi3", "codellama"],
            index=0
        )
        chatbot.model_name = model_choice
        
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
    
    # Display conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Speak to the mountain..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display Mori's response - no spinner for instant feel
        with st.chat_message("assistant"):
            response = chatbot.generate_mori_response(prompt)
            filtered_response = chatbot.apply_mori_filter(response)
            st.markdown(filtered_response)
            st.session_state.messages.append({"role": "assistant", "content": filtered_response})

if __name__ == "__main__":
    main()