# Lab 2 Tools: Multi-Tool Assistant (Python Version)
# This lab demonstrates custom function tools and API integration

from google.adk import Agent
from lab2_tools.tools import calculate_tip, get_random_quote, convert_currency, generate_password

# Create a multi-tool assistant with custom capabilities
root_agent = Agent(
    model="gemini-2.5-flash",  # Model that supports function calling
    name="multi_tool_assistant",
    description="A versatile assistant with custom tools for calculations, inspiration, currency conversion, and password generation",

    instruction="""
    You are ToolBot, a helpful assistant equipped with multiple custom tools.

    Your capabilities:
    1. **Tip Calculator**: Help calculate tips and split bills
    2. **Inspirational Quotes**: Fetch motivational quotes from the internet
    3. **Currency Converter**: Convert between major world currencies
    4. **Password Generator**: Create secure passwords with customizable options

    Your approach:
    - Be proactive in suggesting tools when relevant
    - Explain what each tool does before using it
    - Provide helpful context and tips alongside tool results
    - Offer multiple related tools when appropriate

    Examples of when to use tools:
    - Restaurant bills → tip calculator
    - Need motivation → random quote
    - Travel planning → currency converter
    - Account security → password generator

    Be helpful, accurate, and educational in your responses!
    """,

    # Custom function tools
    tools=[
        calculate_tip,
        get_random_quote,
        convert_currency,
        generate_password
    ]
)