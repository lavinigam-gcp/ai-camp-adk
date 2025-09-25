# Lab 2 Search: Web Search Assistant 🔍

## Overview
This lab demonstrates how to use ADK's built-in Google search tool. You'll build a research assistant that can find current information, verify facts, and help with research tasks using real-time web search capabilities.

## Learning Objectives
- Use built-in ADK tools (google_search)
- Understand when agents should search vs use existing knowledge
- Learn tool integration patterns
- See how agents can cite sources and verify information

## Features Demonstrated
- ✅ Built-in Google search integration
- ✅ Real-time information retrieval
- ✅ Source citation and verification
- ✅ Research assistance capabilities
- ✅ Tool-based decision making

## Files
- `agent.py` - Search assistant implementation
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab2_search** from the dropdown.

## 🗣️ Try These Sample Queries

### **Current Events & News**
```
What's the latest news about artificial intelligence developments?
```

```
What are the recent updates in renewable energy technology?
```

```
Find me information about the latest space exploration missions
```

### **Research & Facts**
```
Who won the Nobel Prize in Physics this year?
```

```
What are the current COVID-19 vaccination rates globally?
```

```
Find information about the latest climate change research findings
```

### **Technology & Innovation**
```
What are the newest features in the latest iPhone release?
```

```
Search for information about quantum computing breakthroughs in 2024
```

```
What are the latest developments in electric vehicle technology?
```

### **Market & Finance**
```
What's Tesla's current stock price and recent performance?
```

```
Find information about cryptocurrency market trends this month
```

```
Search for the latest economic indicators and inflation data
```

### **Education & Learning**
```
Find the best online courses for learning machine learning in 2024
```

```
What are the top programming languages to learn right now?
```

```
Search for information about remote work trends and statistics
```

### **Verification & Fact-Checking**
```
Is it true that a new planet was discovered recently? Find the latest information.
```

```
Verify the claim that solar energy is now cheaper than fossil fuels
```

## Key Concepts

### Built-in Tool Usage
```python
from google.adk.tools import google_search

agent = Agent(
    tools=[google_search]  # Ready-to-use web search
)
```

### When Agents Search
The agent automatically decides when to search based on:
- Current events or time-sensitive information
- Specific facts that might change
- User requests for "latest" or "current" information
- Research tasks requiring verification

### Search Integration
- **Automatic**: Agent decides when to search
- **Contextual**: Searches are relevant to the conversation
- **Cited**: Results include source information
- **Summarized**: Agent presents key findings clearly

## Search Capabilities

### 🌐 Real-time Information
- Latest news and current events
- Stock prices and market data
- Weather and current conditions
- Recent research and discoveries

### 📊 Research Assistance
- Fact verification and checking
- Multiple source comparison
- Trend analysis and statistics
- Academic and technical information

### 🔍 Smart Search Decisions
- Knows when to search vs use training data
- Searches for specific, current information
- Provides context about search results
- Explains when information might be limited

## What's Next?

In Lab 2 Tools, you'll learn how to create custom function tools and combine multiple capabilities in a single agent.

## Tips
- 💡 Ask for "latest" or "current" information to trigger searches
- 💡 Try fact-checking questions to see verification in action
- 💡 Notice how the agent cites sources and timestamps
- 💡 Ask follow-up questions about search results
- 💡 Compare answers about current vs historical topics

## Common Issues
- Search results depend on internet connectivity
- Some queries might return limited results
- Agent will explain when searches don't find relevant information
- Very recent events (last few hours) might not be indexed yet