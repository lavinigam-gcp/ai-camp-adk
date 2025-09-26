# ADK Training Labs - Building Intelligent Agents 🤖

Welcome to the Google Agent Development Kit (ADK) hands-on training session! This repository contains progressive labs designed to teach you how to build intelligent agents using ADK.

## 🎯 Session Overview

**Duration:** 1 hour
**Format:** Hands-on labs with live coding
**Goal:** Master ADK fundamentals and build production-ready agents

## 📋 Prerequisites

1. **Python 3.10+** installed
2. **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/apikey)
3. Basic Python knowledge helpful but not required

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/ai-camp-adk.git
cd ai-camp-adk
```

### 2. Set Up Environment (⚡ Super Fast with uv)
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
# or: pip install uv

# One command setup - creates venv and installs everything!
uv sync

# Activate the environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**Why uv?** It's 10-100x faster than pip and handles everything automatically!

### 3. Configure API Key
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Test Your Setup
```bash
# Run ADK web interface
adk web
```

Visit http://localhost:8000 and select any lab from the dropdown!

## 📚 Lab Structure

### Lab 1: Getting Started - Coffee Shop Assistant ☕
**Time:** 5 mins | **Complexity:** ⭐
- Create your first agent with Python
- Understand instructions and personality
- Learn agent configuration basics

### Lab 1 YAML: Coffee Shop (Configuration Intro) ☕⚙️
**Time:** 5 mins | **Complexity:** ⭐
- Same agent using YAML configuration
- Compare Python vs YAML approaches
- Learn declarative agent creation

### Lab 1 Live: Coffee Shop with Voice/Video 🎙️☕
**Time:** 7 mins | **Complexity:** ⭐⭐
- Experience Gemini Live API
- Real-time voice interactions
- Bidirectional audio streaming

### Lab 2 Search: Web Search Assistant 🔍
**Time:** 5 mins | **Complexity:** ⭐⭐
- Use built-in ADK tools (google_search)
- Research and fact-checking capabilities
- Real-time information retrieval

### Lab 2 Tools: Multi-Tool Assistant 🛠️
**Time:** 7 mins | **Complexity:** ⭐⭐
- Create custom function tools
- API integration (free APIs)
- Error handling and fallbacks

### Lab 3: Multi-Agent Collaboration - Blog Team 👥
**Time:** 8 mins | **Complexity:** ⭐⭐⭐
- Build specialized sub-agents (Writer, Editor)
- Implement agent delegation patterns
- Coordinate team workflows without tools
- **Key Pattern:** Root agent coordinates, sub-agents specialize

### Lab 3 Config: Blog Team (YAML Configuration) 📝⚙️
**Time:** 8 mins | **Complexity:** ⭐⭐⭐
- Same multi-agent system in pure YAML
- Configuration-driven agent definitions
- Compare code vs configuration approaches
- **Architecture:** Clean separation of roles

### Lab 4a: Input Schema Validation - Order Processing 📝
**Time:** 4 mins | **Complexity:** ⭐⭐
- Validate incoming data structure with `input_schema`
- Ensure required fields are present
- Type safety and data validation
- **Pattern:** Structured input processing

### Lab 4b: Output Schema Validation - Weather Data ☀️
**Time:** 4 mins | **Complexity:** ⭐⭐
- Guarantee structured JSON responses with `output_schema`
- Consistent field formatting
- Predictable API responses
- **Pattern:** Reliable data output format

### Lab 5: Stateful Conversations - Learning Tutor 🎓
**Time:** 8 mins | **Complexity:** ⭐⭐⭐
- Implement memory persistence
- Track conversation state
- Personalize interactions

### Lab 6: Workflow Orchestration - Document Pipeline 📄
**Time:** 8 mins | **Complexity:** ⭐⭐⭐⭐
- Use `SequentialAgent` for ordered processing
- Use `ParallelAgent` for concurrent execution
- Use `LoopAgent` for iterative refinement
- **Pattern:** Complex workflow coordination

### Lab 7: Callbacks & Events - Customer Service Monitor 📊
**Time:** 7 mins | **Complexity:** ⭐⭐⭐⭐
- Monitor agent lifecycle with callbacks
- Track performance metrics and timing
- Implement before/after hooks for tools and models
- **Pattern:** Agent monitoring and analytics

### Lab 8: External Integration - File Manager 📁
**Time:** 8 mins | **Complexity:** ⭐⭐⭐⭐⭐
- Integrate external systems via MCP (Model Context Protocol)
- Handle file operations with external tools
- Demonstrate tool confirmation patterns
- **Pattern:** External service integration

## 🎮 Running Labs

### Standard Method (Recommended)
```bash
# Start the web interface
adk web

# Select any lab from the dropdown menu
# ADK automatically detects Python or YAML configuration
```

### Individual Lab Testing
```bash
# For Python implementations
adk run lab1

# For YAML configurations
adk run lab3_config
```

## 🏗️ Project Structure

```
ai-camp-adk/
├── .env.example        # Environment variables template
├── README.md          # This file
├── requirements.txt   # Python dependencies
│
├── lab1/              # Getting Started (Python)
│   ├── agent.py
│   └── README.md
│
├── lab1_yaml/         # Getting Started (YAML Configuration)
│   ├── root_agent.yaml
│   └── README.md
│
├── lab1_live/         # Voice/Video Streaming (Python + Live API)
│   ├── agent.py
│   └── README.md
│
├── lab2_search/       # Web Search Assistant (Python)
│   ├── agent.py
│   └── README.md
│
├── lab2_tools/        # Multi-Tool Assistant (Python)
│   ├── agent.py
│   ├── tools.py
│   └── README.md
│
├── lab3/              # Multi-Agent (Python)
│   ├── agent.py
│   └── README.md
│
├── lab3_config/       # Multi-Agent (YAML Configuration)
│   ├── root_agent.yaml
│   ├── researcher_agent.yaml
│   ├── writer_agent.yaml
│   ├── editor_agent.yaml
│   └── README.md
│
└── lab4-8/           # Remaining labs (Python)
```

## 💡 Key Concepts

### Agent Creation (Python)
```python
from google.adk import Agent

agent = Agent(
    model="gemini-2.0-flash",
    name="my_agent",
    instruction="You are a helpful assistant..."
)
```

### Agent Configuration (YAML)
```yaml
model: gemini-2.0-flash
name: my_agent
instruction: |
  You are a helpful assistant...
```

### Adding Tools
```python
from google.adk.tools import google_search

agent = Agent(
    tools=[google_search, my_custom_function]
)
```

### Multi-Agent Systems
```python
# Key Pattern: Root agent coordinates, sub-agents specialize
root_agent = Agent(
    name="team_lead",
    sub_agents=[writer_agent, editor_agent],  # Specialized roles
    instruction="Coordinate the team workflow..."
)

# Sub-agents focus on single responsibilities
writer_agent = Agent(
    name="writer",
    instruction="Create engaging content...",
    output_key="draft_content"  # Pass data between agents
)
```

**Multi-Agent Architecture Patterns:**
- **Coordinator Pattern**: Root agent manages workflow, delegates tasks
- **Specialist Pattern**: Each sub-agent has one clear responsibility
- **Data Flow**: Use `output_key` to pass results between agents
- **No Tools on Sub-Agents**: Keep tools on root agent to avoid conflicts

## 🛠️ Development Tips

1. **Start Simple**: Begin with Lab 1 and progress sequentially
2. **Use Web Interface**: `adk web` provides the best development experience
3. **Try Voice Features**: Lab 1 Live shows cutting-edge capabilities
4. **Compare Approaches**: See Python vs YAML in Labs 3 vs 3 Config
5. **Check Logs**: Use browser dev tools for debugging

## 🐛 Troubleshooting

### Common Issues

**Setup Issues with uv**
```bash
# If uv is not installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# If dependencies aren't installing
uv sync --reinstall

# Alternative: use pip if uv issues persist
pip install -r requirements.txt
```

**API Key Not Working**
```bash
# Verify your key is set
echo $GOOGLE_API_KEY

# Test with a simple call
python -c "from google import genai; genai.configure(api_key='YOUR_KEY'); print('OK')"
```

**Lab Not Appearing in Dropdown**
- Ensure you're running `adk web` from the repository root
- Check that the lab folder contains either `agent.py` or `root_agent.yaml`
- Verify the `__init__.py` file exists in Python-based labs

**Voice Features Not Working (Lab 1 Live)**
- Use Chrome or Edge browser
- Allow microphone/camera permissions
- Check internet connection stability
- Verify Gemini Live API access

## 📖 Resources

- [ADK Documentation](https://github.com/google/adk-python)
- [Gemini API Docs](https://ai.google.dev/docs)
- [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api)
- [Google AI Studio](https://aistudio.google.com)

## 📝 Session Flow

### Introduction (5 mins)
- ADK overview and architecture
- Setup verification
- Web interface walkthrough

### Foundation Labs (26 mins) - Labs 1-3
- Basic agents (Lab 1 Python + Lab 1 YAML)
- Voice capabilities (Lab 1 Live)
- Search tools (Lab 2 Search)
- Custom tools (Lab 2 Tools)
- Multi-agent systems (Lab 3)
- Configuration approach (Lab 3 Config)

### Intermediate Labs (16 mins) - Labs 4a, 4b, 5
- Input validation (Lab 4a)
- Output validation (Lab 4b)
- State management and memory (Lab 5)

### Advanced Labs (18 mins) - Labs 6-8
- Workflow orchestration (Lab 6)
- Callbacks and monitoring (Lab 7)
- External integrations (Lab 8)

## 🎉 Congratulations!

By completing these labs, you've learned:
- ✅ Creating agents with Python and YAML
- ✅ Voice/video streaming with Live API
- ✅ Adding tools and capabilities
- ✅ Building multi-agent systems
- ✅ Managing state and memory
- ✅ Implementing workflows
- ✅ Monitoring with callbacks
- ✅ Integrating external services

You're now ready to build production-ready AI agents with ADK!

## 🧪 Quick Test Examples

### Lab 1: Basic Agent
- "Can you recommend a coffee for someone who likes strong flavors?"
- "What pastries do you have available?"

### Lab 1 Live: Voice Assistant
- Enable microphone and speak: "What's your most popular drink?"
- Try voice commands for natural conversation

### Lab 2 Search: Web Search
- "What are the latest developments in AI?"
- "Search for information about quantum computing"

### Lab 2 Tools: Multi-Tool Assistant
- "Calculate a 18% tip on $45.67"
- "Convert 100 USD to EUR"
- "Generate a secure password"

### Lab 3: Multi-Agent Blog Team
- "Write a blog post about remote work benefits"
- "Create an article about sustainable technology trends"

### Lab 4a: Input Schema Validation
```json
{
  "customer_name": "Sarah",
  "items": "1 Pizza, 2 Coffee",
  "order_type": "takeout",
  "dietary_restrictions": "vegetarian"
}
```

### Lab 4b: Output Schema Validation
- "What's the weather in San Jose?"
- "Give me weather data for Cupertino"

### Lab 5: Stateful Learning Tutor
- "I want to learn Python programming"
- "Can you help me with machine learning basics?"

### Lab 6: Workflow Orchestration
- "Process this document: [paste any text]"
- Demonstrates sequential → parallel → loop processing

### Lab 7: Callbacks & Monitoring
- "I have a complaint about my order"
- Watch the callback metrics in the logs

### Lab 8: External Integration
- "List the files in my directory"
- "Help me organize my documents"

## 🤝 Contributing

Found an issue or have an improvement? We welcome contributions!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Support

- **Issues:** [GitHub Issues](https://github.com/your-org/ai-camp-adk/issues)
- **Discussions:** [GitHub Discussions](https://github.com/your-org/ai-camp-adk/discussions)
- **ADK Community:** [Official ADK Repository](https://github.com/google/adk-python)

---

**Happy Building! 🚀**

*Built with ❤️ using Google Agent Development Kit*