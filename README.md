# Simple AI Agent with LangGraph

A Python-based AI agent built using LangChain and LangGraph that can perform real-time calculations and chat via OpenRouter.

## 🎯 Intended Learning Outcomes (ILO)

By completing this project, you will have learned how to:
- **Build an AI Agent**: Use `langchain` and `langgraph` to create an autonomous agent.
- **Integrate Tools**: Create custom Python functions (like the `calculator`) and register them as tools for an AI to use.
- **Manage API Connections**: Securely connect to LLM providers using OpenRouter and environment variables.
- **Handle Streaming**: Implement real-time token streaming for a smoother "typing" effect in the terminal.
- **Modern Python Tooling**: Use `uv` for lightning-fast dependency management and virtual environments.
- **Security Best Practices**: Protect API keys using `.gitignore` and `.env` patterns.

## 🛠️ Setup & Installation

### 1. Initialize the project
This project uses `uv` for dependency management.
```bash
uv init .
```

### 2. Install Dependencies
```bash
uv add langgraph langchain python-dotenv langchain-openai langchain-core
```

### 3. Environment Configuration
1. Create a `.env` file in the root directory.
2. Add your OpenRouter API key:
   ```bash
   OPENAI_API_KEY=your_openrouter_key_here
   ```
*(A `.env.example` file is provided as a template.)*

## 🚀 Running the Agent

To start the interactive agent, run:
```bash
uv run python main.py
```

### Features to try:
- **Direct Chat**: Just say "Hi" or ask "How are you?".
- **Math Operations**: Ask "What is 15 multiplied by 4?" or "Divide 100 by 5".
- **Streaming**: Watch the assistant's reply appear in real-time.
- **Exit**: Type `quit` to close the session.

## 🧮 How the Calculator Works
The agent uses a custom Python tool decorated with `@tool`. When you ask a math question, the AI identifies that the `calculator` tool is needed, extracts the numbers and the operation, and executes the local Python code to ensure 100% mathematical accuracy.

## 📝 Technical Notes
- **Provider**: OpenRouter.ai (GPT-4o-mini)
- **Framework**: LangChain Agents (moving towards LangGraph V2 standards)
- **Streaming**: Enabled via `stream_mode="messages"`
