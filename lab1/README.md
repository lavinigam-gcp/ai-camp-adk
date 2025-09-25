# Lab 1: Getting Started - Coffee Shop Assistant ☕

## Overview
Welcome to your first ADK lab! In this lab, you'll create a friendly coffee shop assistant that can help customers with menu questions and recommendations. This lab introduces the fundamental concepts of ADK agents.

## Learning Objectives
- Create your first ADK agent using both Python and YAML
- Understand core agent properties: model, name, description, and instructions
- Learn how instructions shape agent personality and behavior
- See the difference between code-based and config-based agents

## Features Demonstrated
- ✅ Basic agent creation
- ✅ Model selection (Gemini 2.5 Flash)
- ✅ Agent identity (name & description)
- ✅ Instruction engineering
- ✅ Both Python and YAML approaches

## Files
- `agent.py` - Python implementation
- `root_agent.yaml` - YAML configuration implementation
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab1** from the dropdown. ADK automatically detects the Python implementation.

## 🗣️ Try These Sample Queries

Copy and paste these queries to interact with your coffee shop assistant:

### **Getting Started**
```
Hi there! What do you recommend for someone new to coffee?
```

### **Morning Rush**
```
I'm running late but need something strong to wake me up. What's quick and caffeinated?
```

### **Dietary Preferences**
```
I'm trying to cut back on caffeine but still want something warm and tasty. Any suggestions?
```

### **Sweet Tooth**
```
I have a major sweet tooth today. What drink and pastry combo would you recommend?
```

### **Budget Conscious**
```
I'm on a tight budget but really need my coffee fix. What's your most affordable option?
```

### **Coffee Curious**
```
What's the difference between a cappuccino and a latte? Which should I try?
```

### **Loyalty Program**
```
Tell me about your loyalty program. How does it work?
```

### **Fun Conversation**
```
Share a fun coffee fact with me! I love learning about coffee.
```

### **Special Orders**
```
Can you make me something special that's not on the menu?
```

### **Weather-Based**
```
It's really cold outside today. What would warm me up?
```

## Key Concepts

### Model Selection
```python
model="gemini-2.5-flash"  # Fast, efficient model for interactive agents
```

### Agent Identity
```python
name="coffee_shop_assistant"  # Unique identifier
description="A friendly coffee shop assistant..."  # Purpose statement
```

### Instructions
Instructions are the heart of your agent's behavior. They define:
- **Role**: Who the agent is (Café, a coffee shop assistant)
- **Knowledge**: What the agent knows (menu, prices, specials)
- **Personality**: How the agent behaves (warm, enthusiastic)
- **Process**: Steps to follow when interacting

## Python vs YAML

### When to use Python (`agent.py`):
- Need dynamic configuration
- Want to add custom logic
- Integrating with existing Python code
- Need full programming capabilities

### When to use YAML (`root_agent.yaml`):
- Simple, static configurations
- Non-programmers maintaining agents
- Version control friendly
- Clear, readable structure

## What's Next?

In Lab 2, you'll learn how to add tools and capabilities to make your agent more powerful. Your coffee shop assistant will be able to:
- Search for coffee recipes online
- Calculate prices and discounts
- Check real weather for iced drink recommendations

## Tips
- 💡 Try modifying the instructions to change the agent's personality
- 💡 Add new menu items and see how the agent handles them
- 💡 Experiment with different greetings and responses
- 💡 Notice how the agent maintains context throughout the conversation

## Common Issues
- If the agent doesn't start, check that your `.env` file has a valid `GOOGLE_API_KEY`
- Make sure you're running from the repository root, not inside the lab folder
- The agent should respond naturally - if responses seem off, check the instruction formatting