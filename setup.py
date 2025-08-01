"""
Setup script for Mori Buntarou Chatbot
Prepares the environment and downloads necessary models
"""

import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def check_ollama():
    """Check if Ollama is installed and running"""
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ollama is installed and running")
            return True
        else:
            print("❌ Ollama is not running")
            return False
    except FileNotFoundError:
        print("❌ Ollama is not installed")
        print("Please install Ollama from: https://ollama.ai/")
        return False

def pull_models():
    """Pull necessary Ollama models"""
    models = ["mistral", "llama3"]
    
    for model in models:
        print(f"🔄 Pulling {model} model...")
        try:
            subprocess.run(["ollama", "pull", model], check=True)
            print(f"✅ {model} model ready")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to pull {model} model")

def main():
    print("🏔️ Setting up Mori Buntarou Mountain Chatbot")
    print("=" * 50)
    
    # Install Python requirements
    install_requirements()
    
    # Check Ollama
    if not check_ollama():
        print("\n⚠️  Please install and start Ollama first:")
        print("1. Download from https://ollama.ai/")
        print("2. Install and start the service")
        print("3. Run this setup script again")
        return
    
    # Pull models
    pull_models()
    
    print("\n🎉 Setup complete!")
    print("\nTo start the chatbot:")
    print("streamlit run mori_chatbot.py")
    print("\nThe mountain awaits your questions...")

if __name__ == "__main__":
    main()