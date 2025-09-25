# Lab 3: Multi-Agent Collaboration - Blog Creation Team 👥

## Overview
This lab introduces multi-agent systems where specialized agents collaborate to complete complex tasks. You'll build a blog creation team with a researcher, writer, and editor working together. This demonstrates agent delegation, data passing, and orchestration.

## Learning Objectives
- Create specialized sub-agents with specific roles
- Understand agent delegation and orchestration
- Learn how agents pass data using `output_key`
- Use state variables in instructions with `{variable}` syntax
- See how complex tasks benefit from agent specialization

## Features Demonstrated
- ✅ Multi-agent architecture
- ✅ Agent delegation patterns
- ✅ Data passing via output_key
- ✅ State variable interpolation
- ✅ Specialized agent roles
- ✅ Sequential task coordination

## Files
- `agent.py` - Python implementation of the blog team
- `root_agent.yaml` - YAML root agent configuration
- `researcher_agent.yaml` - YAML researcher configuration
- `writer_agent.yaml` - YAML writer configuration
- `editor_agent.yaml` - YAML editor configuration
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab3** from the dropdown.

## 🗣️ Try These Sample Queries

### **Technology & Innovation**
```
Write a blog post about the future of artificial intelligence and its impact on daily life
```

```
Create content explaining quantum computing for beginners - make it easy to understand
```

```
Write about sustainable technology trends that are changing the world
```

### **Business & Career**
```
Create a blog about remote work best practices for distributed teams
```

```
Write about startup funding strategies - what entrepreneurs need to know in 2024
```

```
Create content on digital transformation for small and medium businesses
```

### **Health & Lifestyle**
```
Write a blog post about mindfulness and mental health in the digital age
```

```
Create content about sustainable living tips that anyone can implement
```

```
Write about achieving work-life balance in a hyperconnected world
```

### **Creative Challenges**
```
Write a blog post about the history and cultural significance of coffee around the world
```

```
Create content explaining blockchain technology and cryptocurrency for complete beginners
```

**Watch the Process:** You'll see the team collaborate - researcher gathers info, writer creates content, editor polishes it!

## How It Works

### The Team Workflow

```
User Request → Team Lead → Researcher → Writer → Editor → Final Content
                   ↓           ↓          ↓         ↓
                Coordinates  Gathers   Creates   Polishes
                            research    draft    content
```

### Data Flow

1. **Researcher** outputs to `research_data`
2. **Writer** reads `{research_data}` and outputs to `draft_content`
3. **Editor** reads `{draft_content}` and outputs to `final_content`
4. **Team Lead** presents the final result

## Key Concepts

### Agent Specialization
Each agent has a focused role:
```python
researcher_agent = Agent(
    name="researcher",
    description="Expert at researching topics...",
    tools=[google_search],  # Has search capability
    output_key="research_data"  # Saves findings
)
```

### Data Passing with output_key
```python
output_key="research_data"  # Agent stores its output here
```

### State Variables in Instructions
```python
instruction="""
    Use the research data provided: {research_data}
    ...
"""
```
The `{research_data}` gets replaced with actual data from state.

### Agent Delegation
```python
sub_agents=[researcher_agent, writer_agent, editor_agent]
```

## Multi-Agent Patterns

### Sequential Processing
- Research → Write → Edit
- Each step depends on the previous

### Specialized Roles
- **Researcher**: Information gathering, fact-checking
- **Writer**: Creative content generation
- **Editor**: Quality control, polish

### Coordinated Workflow
- **Team Lead**: Orchestrates and monitors progress

## Extending This Lab

### Add More Specialists:
1. **SEO Optimizer**: Optimize for search engines
2. **Fact Checker**: Verify all claims
3. **Translator**: Create multilingual versions
4. **Social Media**: Create social posts from blog

### Try Different Workflows:
1. **Parallel Research**: Multiple researchers on subtopics
2. **Iterative Editing**: Writer-Editor feedback loop
3. **A/B Testing**: Multiple writers, choose best

## Python vs YAML

### Python Advantages:
- Dynamic agent creation
- Conditional sub-agents
- Programmatic configuration

### YAML Advantages:
- Clear hierarchy visualization
- Easy agent swapping
- Non-programmer friendly

## What's Next?

In Lab 4, you'll learn about structured data with input/output schemas. You'll build a restaurant order system that:
- Accepts structured order requests
- Validates against menu schema
- Returns structured receipts
- Handles complex order modifications

## Tips
- 💡 Each agent should have one clear responsibility
- 💡 Use descriptive output_key names
- 💡 State variables persist within a session
- 💡 Agents can read any state variable, not just their inputs
- 💡 The root agent sees all sub-agent activities

## Common Issues
- If agents don't see previous outputs, check output_key names
- Ensure state variable names in instructions match exactly (case-sensitive)
- Sub-agents must be defined before the root agent in Python
- YAML configs need correct relative paths for sub-agents