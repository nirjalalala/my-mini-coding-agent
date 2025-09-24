# Agentic AI Code Editor (Toy Claude Code)

A lightweight **CLI AI code editor** inspired by Cursor and Claude Code, built using **Google’s free Gemini API**.  
This project demonstrates how a Large Language Model (LLM) can function as a simple coding agent.

## 🚀 Features
- Accepts natural language coding tasks (e.g., *"Fix string splitting in my app"*).
- Uses predefined actions to:
  - Scan directories
  - Read file contents
  - Edit/overwrite files
  - Execute Python code
- Iteratively works to complete tasks or provide helpful feedback.

## 🛠️ Tech Stack
- **Python 3.10+**
- **Google Gemini API** (free tier)

## 📦 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agentic-ai-editor.git
   cd agentic-ai-editor
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Gemini API key**  
   - Create a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Export it as an environment variable:
     ```bash
     export GEMINI_API_KEY="your_api_key_here"   # Linux/Mac
     set GEMINI_API_KEY="your_api_key_here"      # Windows
     ```

## ▶️ Usage
Run the CLI tool and describe a coding task:
```bash
python main.py "Fix the bug in my file parser"
```

The agent will:
1. Analyze your request.
2. Choose appropriate predefined actions.
3. Attempt to modify or run code to solve the task.

## ⚠️ Disclaimer
This is a **toy project** for learning and experimentation.  
The AI may make mistakes or overwrite files—use with caution.

