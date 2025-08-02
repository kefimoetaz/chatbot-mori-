
🏔️ Mori Buntarou Mountain Chatbot
An interactive AI chatbot that embodies Mori Buntarou, a stoic mountain climber character, featuring authentic personality modeling and comprehensive mountaineering knowledge. Built with local LLM integration and a manga-inspired interface.



🎯 Features
⚡ Lightning-Fast Responses - Optimized local LLM for sub-second replies
🎭 Authentic Character AI - Captures Mori's stoic, introverted personality
🎨 Manga-Style Interface - Clean speech bubbles with visual flair
🗻 Comprehensive Knowledge - Extensive mountain climbing database
🔒 Privacy-Focused - Runs entirely on your local machine
📱 Responsive Design - Works on desktop and mobile devices
🖼️ Screenshots
┌─────────────────────────────────────────┐
│  🏔️ Mori Buntarou                      │
│  The Solitary Climber's Wisdom         │
│  "In silence, the mountain speaks"      │
├─────────────────────────────────────────┤
│  💬 User: "What's the best climbing     │
│      technique for beginners?"          │
│                                         │
│  🗨️ Mori: "Start with top rope. Learn  │
│      to fall before you learn to fly."  │
└─────────────────────────────────────────┘
🚀 Quick Start
Prerequisites
Python 3.10 or higher
Ollama installed and running
At least one language model (recommended: llama3.2:1b)
Installation
Clone the repository

git clone https://github.com/kefimoetaz/mori-chatbot.git
cd mori-chatbot
Install dependencies

pip install -r requirements.txt
Install and start Ollama

# Install Ollama from https://ollama.ai/
# Pull a language model
ollama pull llama3.2:1b
Run the application

streamlit run mori_chatbot.py
Open your browser Navigate to http://localhost:8501

📁 Project Structure
mori-chatbot/
├── mori_chatbot.py          # Main application
├── mori_persona.py          # Character personality & prompts
├── mountain_knowledge.py    # Climbing knowledge database
├── requirements.txt         # Python dependencies
├── setup.py                # Setup script
├── logo.png                # Character logo (optional)
├── bg.jpeg                 # Background image (optional)
└── README.md               # This file
🛠️ Tech Stack
| Technology | Purpose | Version | |------------|---------|---------| | Python | Core application logic | 3.10+ | | Streamlit | Web interface framework | 1.28+ | | Ollama | Local LLM runtime | Latest | | CSS3 | Custom styling & animations | - | | HTML5 | Semantic markup | - |

⚙️ Configuration
Supported Models
llama3.2:1b (recommended for speed)
mistral
llama3
phi3
codellama
Customization
Character Personality (mori_persona.py):

MORI_SYSTEM_PROMPT = """You are Mori Buntarou, a solitary climber..."""
Mountain Knowledge (mountain_knowledge.py):

MOUNTAIN_DATA = {
    "techniques": {...},
    "equipment": {...},
    "weather": {...}
}
Visual Assets:

Replace logo.png with your character image
Replace bg.jpeg with your background image
🎨 Interface Features
Manga-Style Design
Speech Bubbles: Authentic manga-style chat interface
Character Consistency: Visual design matches personality
Responsive Layout: Adapts to different screen sizes
Performance Optimizations
Fast Responses: Sub-second reply times
Minimal Loading: No spinners or delays
Efficient Memory: Optimized session management
📚 Knowledge Base
The chatbot includes comprehensive information about:

🧗 Climbing Techniques: Free solo, alpine, ice, mixed climbing
🎒 Equipment: Ropes, protection, clothing, tools
🌤️ Weather: Mountain conditions, seasonal patterns
⚠️ Hazards: Objective and subjective dangers
🏔️ Famous Peaks: Everest, K2, Matterhorn, Japanese mountains
🗾 Japanese Mountains: Fuji, Yari, Hotaka with cultural context
🔧 Development
Running in Development Mode
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
streamlit run mori_chatbot.py --server.runOnSave true
Adding New Knowledge
Edit mountain_knowledge.py
Add new categories or expand existing ones
Update search functionality if needed
Customizing Character
Modify mori_persona.py
Adjust system prompts and response patterns
Test character consistency
🚀 Deployment
Local Deployment
streamlit run mori_chatbot.py --server.port 8501
Docker Deployment
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "mori_chatbot.py"]
🤝 Contributing
Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
Contribution Guidelines
Follow Python PEP 8 style guide
Add docstrings to new functions
Test character consistency
Update documentation as needed
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ollama Team - For the excellent local LLM runtime
Streamlit - For the intuitive web framework
Mountain Climbing Community - For knowledge and inspiration
Manga Artists - For visual design inspiration
📞 Support
Issues: GitHub Issues
Discussions: GitHub Discussions
Email: kefiimoetaz@gmail.com
🔮 Roadmap
[ ] Voice integration for audio responses
[ ] Real-time weather data integration
[ ] Interactive route planning features
[ ] Mobile app version
[ ] Multi-language support
[ ] Community sharing features
Built with ❤️ for the climbing community

"In silence, the mountain speaks" - Mori Buntarou







