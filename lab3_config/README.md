# Lab 3 Config: Multi-Agent Blog Team (YAML Configuration) 📝⚙️

## Overview
This lab demonstrates the power of YAML-based agent configuration for complex multi-agent systems. You'll see how to build a sophisticated blog creation team using pure configuration files, showcasing ADK's declarative approach to agent orchestration.

## Learning Objectives
- Master YAML-based agent configuration
- Understand config-driven multi-agent architecture
- Compare code vs configuration approaches
- See complex agent personalities in YAML
- Learn advanced config features (sub_agents, output_key, state variables)

## Features Demonstrated
- ✅ Pure YAML configuration (no Python code)
- ✅ Complex multi-agent orchestration
- ✅ Professional agent personalities
- ✅ State variable interpolation
- ✅ Config-based tool integration
- ✅ Declarative workflow definition

## Files
- `root_agent.yaml` - Team lead orchestrator
- `researcher_agent.yaml` - Research specialist with web search
- `writer_agent.yaml` - Content creation expert
- `editor_agent.yaml` - Quality assurance specialist
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```

Then select **lab3_config** from the dropdown. ADK automatically detects YAML configuration.

## YAML Configuration Highlights

### Professional Agent Personas
Each agent has a detailed professional identity:
```yaml
instruction: |
  You are Dr. Sarah Chen, a meticulous research specialist with expertise in:
  - Academic research methodology
  - Fact verification and source validation
  - Current trends and developments analysis
```

### State Variable Usage
Agents reference previous outputs:
```yaml
instruction: |
  Use the research provided: {research_brief}
  Review this draft: {draft_article}
```

### Tool Integration
Built-in tools via configuration:
```yaml
tools:
  - name: google_search
```

### Sub-Agent Orchestration
```yaml
sub_agents:
  - config_path: researcher_agent.yaml
  - config_path: writer_agent.yaml
  - config_path: editor_agent.yaml
```

## Try These Blog Topics

### 1. Technology Topics:
- "Write about the future of quantum computing"
- "Create content on sustainable technology trends"
- "Explain blockchain technology for beginners"

### 2. Business Content:
- "Write about remote work productivity strategies"
- "Create content on startup funding landscape"
- "Explain digital transformation for SMBs"

### 3. Science Topics:
- "Write about recent space exploration achievements"
- "Create content on climate change solutions"
- "Explain CRISPR gene editing simply"

## Configuration vs Code Comparison

| Aspect | Lab 3 (Python) | Lab 3 Config (YAML) |
|--------|----------------|----------------------|
| **Setup** | Import statements, function definitions | Pure configuration |
| **Maintenance** | Requires Python knowledge | Accessible to non-programmers |
| **Readability** | Mixed code/config | Clear, declarative |
| **Debugging** | Python debugging tools | Config validation |
| **Flexibility** | Full programming power | Structured constraints |
| **Deployment** | Code + config | Config only |

## Advanced YAML Features

### 1. Multi-line Instructions
```yaml
instruction: |
  Your multi-line instruction
  with proper formatting
  and structure
```

### 2. State References
```yaml
instruction: "Process this data: {previous_output}"
```

### 3. Nested Configuration
```yaml
sub_agents:
  - config_path: sub_agent.yaml
    custom_params: value
```

### 4. Tool Configuration
```yaml
tools:
  - name: google_search
  - name: my_module.custom_function
```

## YAML Best Practices

### ✅ DO:
- Use descriptive agent names
- Include detailed instructions
- Leverage state variables
- Document complex logic
- Use consistent formatting

### ❌ DON'T:
- Mix tabs and spaces
- Use complex nested structures unnecessarily
- Skip instruction documentation
- Hardcode dynamic values

## When to Use YAML Config

### **Choose YAML when:**
- Non-programmers need to maintain agents
- Simple, predictable workflows
- Rapid prototyping and testing
- Clear separation of concerns
- Version control of agent behavior

### **Choose Python when:**
- Complex conditional logic needed
- Dynamic agent creation
- Custom tool implementations
- Advanced error handling
- Integration with existing codebases

## What's Next?

In Lab 4, you'll work with structured data using Pydantic schemas. This adds:
- Input validation and schemas
- Output format enforcement
- Type safety and documentation
- Complex data structure handling

## Key Takeaways
- 💡 YAML configuration can handle complex multi-agent scenarios
- 💡 Professional agent personas improve output quality
- 💡 State variables enable sophisticated data flow
- 💡 Configuration is often more maintainable than code
- 💡 Different approaches suit different use cases

## Tips
- Study the YAML structure to understand the data flow
- Notice how professional personas affect agent behavior
- Compare the output quality with Lab 3 Python version
- Try modifying agent personalities in the YAML files
- See how easy it is to swap out team members by changing config paths

## Troubleshooting
- **YAML syntax errors**: Check indentation (use spaces, not tabs)
- **Agent not found**: Verify config_path references
- **State variables empty**: Check output_key names match instruction references
- **Tools not working**: Ensure proper tool name formatting