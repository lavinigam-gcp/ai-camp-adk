# Lab 1 YAML: Coffee Shop Assistant (Configuration Intro) ☕⚙️

## Overview
This lab introduces YAML-based agent configuration - the same coffee shop assistant from Lab 1, but built using pure configuration instead of Python code. Perfect for understanding ADK's declarative approach to agent creation.

## Learning Objectives
- Understand YAML configuration basics
- Compare Python vs YAML approaches
- Learn configuration syntax and structure
- See when to use config vs code
- Master the fundamentals of declarative agents

## Features Demonstrated
- ✅ YAML-based agent creation
- ✅ Multi-line instruction formatting
- ✅ Configuration-driven personality
- ✅ No code required
- ✅ Easy maintenance and updates

## Files
- `root_agent.yaml` - Complete agent configuration
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```

Then select **lab1_yaml** from the dropdown. ADK automatically detects YAML configuration.

## YAML Configuration Breakdown

### Basic Agent Properties
```yaml
model: gemini-2.0-flash        # Model selection
name: coffee_shop_assistant    # Agent identifier
description: A friendly coffee shop assistant...  # Purpose statement
```

### Multi-line Instructions
```yaml
instruction: |
  You are Café, a warm and friendly coffee shop assistant...

  Your personality:
  - Be warm, welcoming, and enthusiastic
  - Make personalized recommendations
```

The `|` symbol preserves line breaks and formatting.

## 🗣️ Try These Sample Queries

Use the same queries as Lab 1 to compare behavior:

### **Getting Started**
```
Hi there! What do you recommend for someone new to coffee?
```

### **Morning Rush**
```
I'm running late but need something strong to wake me up. What's quick and caffeinated?
```

### **Coffee Education**
```
What's the difference between a cappuccino and a latte? Which should I try?
```

### **Loyalty Program**
```
Tell me about your loyalty program. How does it work?
```

### **Fun Facts**
```
Share a fun coffee fact with me! I love learning about coffee.
```

**Notice:** The behavior should be identical to Lab 1 (Python version) - same responses, same personality!

## Python vs YAML Comparison

| Aspect | Lab 1 (Python) | Lab 1 YAML (Config) |
|--------|-----------------|----------------------|
| **Code Required** | Python imports & syntax | None |
| **File Type** | `.py` | `.yaml` |
| **Maintenance** | Requires Python knowledge | Anyone can edit |
| **Dynamic Logic** | Full programming power | Configuration only |
| **Readability** | Mixed code/config | Pure declarative |
| **Version Control** | Code + logic changes | Config changes only |

## When to Use YAML Configuration

### ✅ **Choose YAML when:**
- Simple, static agent behavior
- Non-programmers need to maintain agents
- Quick prototyping and testing
- Clear separation of concerns
- Easy A/B testing of personalities

### ✅ **Choose Python when:**
- Dynamic logic required
- Complex tool integrations
- Conditional behavior needed
- Custom error handling
- Advanced programming constructs

## YAML Best Practices

### Structure
```yaml
# Use clear, descriptive names
name: coffee_shop_assistant

# Multi-line instructions with proper formatting
instruction: |
  Your detailed instructions here
  with proper line breaks
  and clear structure
```

### Comments
```yaml
# Use comments to explain complex configurations
model: gemini-2.0-flash  # Fast model for interactive chat
```

### Consistency
- Use consistent indentation (2 spaces recommended)
- Follow naming conventions
- Keep instructions well-organized

## What's Next?

In Lab 2, you'll add tools to your agents. While this simple example uses pure configuration, more complex agents often benefit from Python's flexibility for:
- Custom tool creation
- Dynamic behavior
- Advanced integrations

## Key Takeaways
- 💡 YAML configuration is perfect for simple, maintainable agents
- 💡 No programming knowledge required to modify behavior
- 💡 Same functionality as Python version with cleaner syntax
- 💡 Great for rapid prototyping and non-technical team members
- 💡 ADK automatically detects and loads YAML configurations

## Tips
- Notice how clean and readable the configuration is
- Try modifying the personality in the YAML file
- Compare the agent behavior with Lab 1 - should be identical
- Experiment with different instruction formats
- See how easy it is to maintain without code knowledge

## Troubleshooting
- **YAML syntax errors**: Check indentation (use spaces, not tabs)
- **Agent not loading**: Verify YAML formatting with a validator
- **Instructions not working**: Check the `|` symbol for multi-line text
- **Behavior differences**: Both labs should behave identically