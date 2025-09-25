# Lab 2 Tools: Multi-Tool Assistant 🛠️

## Overview
This lab demonstrates how to create custom function tools in ADK. You'll build an assistant equipped with multiple tools including tip calculation, API integration for quotes, currency conversion, and password generation.

## Learning Objectives
- Create custom function tools with proper documentation
- Integrate free APIs without authentication
- Handle errors gracefully in tool functions
- Use multiple tools in one agent
- Understand tool design best practices

## Features Demonstrated
- ✅ Custom function tools
- ✅ API integration (Quotable API)
- ✅ Error handling and fallbacks
- ✅ Structured tool responses
- ✅ Multi-tool coordination

## Files
- `agent.py` - Multi-tool assistant implementation
- `tools.py` - Custom tool definitions
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab2_tools** from the dropdown.

## 🗣️ Try These Sample Queries

### **Tip Calculator**
```
My restaurant bill is $85 and the service was excellent. How much should I tip?
```

```
Calculate a 20% tip on a $120 bill and split it between 4 people
```

```
Help me figure out the tip for a $67.50 dinner bill with 18% gratuity
```

### **Inspirational Quotes (API)**
```
I need some motivation for my day. Can you get me an inspirational quote?
```

```
Give me a quote about success to inspire my team
```

```
I'm feeling down. Can you share something uplifting?
```

### **Currency Conversion**
```
Convert 100 USD to Euros
```

```
How much is 5000 Japanese Yen in British Pounds?
```

```
I have $500 for my trip to Switzerland. What's that in Swiss Francs?
```

### **Password Generation**
```
Generate a secure password for my new account
```

```
Create a 16-character password with special symbols for banking
```

```
I need a simple 8-character password without symbols for my wifi
```

### **Multi-Tool Scenarios**
```
I'm planning a dinner in Paris. The meal costs 80 Euros, help me budget for the total cost in USD including tip
```

```
Create a secure password for me and then give me a motivational quote about cybersecurity
```

```
I'm traveling to Japan with $1000. Convert it to Yen and give me a travel quote for inspiration
```

## Key Concepts

### Custom Tool Structure
```python
def tool_name(param: type) -> Dict[str, Any]:
    """
    Clear description of what the tool does.

    Args:
        param: Description of parameter

    Returns:
        Dictionary with structured response
    """
    # Tool implementation
    return {"result": "data"}
```

### API Integration
```python
# Free API call without authentication
response = requests.get("https://api.quotable.io/random")
data = response.json()
```

### Error Handling
```python
try:
    # API call or operation
    result = api_operation()
except Exception as e:
    # Graceful fallback
    return {"error": str(e), "fallback": "default_value"}
```

## Tool Capabilities

### 💰 Tip Calculator
- Calculates tip amounts and totals
- Supports different tip percentages
- Provides split-bill calculations
- Formats currency properly

### 💡 Quote API Integration
- Fetches real quotes from Quotable API
- No API key required
- Graceful fallback for network issues
- Returns structured quote data

### 💱 Currency Converter
- Supports major world currencies
- Simplified exchange rates for demo
- Clear rate information
- Error handling for unsupported currencies

### 🔐 Password Generator
- Customizable length and complexity
- Strength assessment
- Security recommendations
- Safe character set handling

## Tool Design Best Practices

### ✅ DO:
- Use clear, descriptive function names
- Include comprehensive docstrings
- Return structured dictionaries
- Handle errors gracefully
- Provide helpful error messages
- Use type hints

### ❌ DON'T:
- Return unstructured strings
- Skip error handling
- Use ambiguous parameter names
- Forget documentation
- Make unvalidated API calls

## What's Next?

In Lab 3, you'll learn about multi-agent systems where specialized agents collaborate using their own tools and expertise.

## Tips
- 💡 Tools automatically get called based on user intent
- 💡 Try combining multiple tools in one request
- 💡 Notice how errors are handled gracefully
- 💡 The quote tool demonstrates real API integration
- 💡 Tools return structured data for better responses

## Common Issues
- Network errors with quote API (fallback quote provided)
- Currency conversion uses simplified demo rates
- Password tool ensures minimum security requirements
- Tools validate input parameters automatically