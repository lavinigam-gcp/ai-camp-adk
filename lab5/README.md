# Lab 5: Stateful Conversations - Personal Learning Tutor 🎓

## Overview
This lab demonstrates state management and memory persistence in ADK agents. You'll build a personal learning tutor that remembers your progress, tracks topics covered, and personalizes the learning experience based on your history.

## Learning Objectives
- Implement memory persistence in agents
- Track conversation state across sessions
- Use state variables in instructions
- Create personalized learning experiences
- Understand memory tools and storage

## Features Demonstrated
- ✅ Memory persistence and recall
- ✅ Progress tracking and analytics
- ✅ State variable interpolation
- ✅ Custom memory tools
- ✅ Personalized interactions
- ✅ Learning streak tracking

## Files
- `agent.py` - Learning tutor with memory capabilities
- `memory_tools.py` - Custom memory management tools
- `README.md` - This file

## Running the Lab

```bash
# From the repository root
adk web
```
Then select **lab5** from the dropdown.

## 🗣️ Try These Sample Queries

### **Getting Started**
```
Hi Luna! I'm new here. What can you help me learn today?
```

```
I'm interested in learning Python programming. Where should we start?
```

### **Learning Sessions**
```
Can you teach me about machine learning basics?
```

```
I want to understand how databases work. Can you explain?
```

```
Help me learn about web development - HTML, CSS, and JavaScript
```

### **Quiz & Assessment**
```
Can you quiz me on what we learned about Python variables?
```

```
Test my knowledge of machine learning concepts we discussed
```

```
I think I understand loops now. Can you give me a quick quiz?
```

### **Progress Tracking**
```
What topics have we covered so far in our sessions?
```

```
How am I doing with my learning progress?
```

```
What should I review based on my quiz scores?
```

### **Personalization**
```
I learn better with visual examples. Can you remember that for our future sessions?
```

```
I prefer to learn at a slower pace with lots of practice. Please adjust your teaching style.
```

```
I'm more of a hands-on learner. Can you give me practical exercises?
```

### **Advanced Learning**
```
I've been learning for a week now. What advanced topics should I tackle next?
```

```
Based on my progress, what are my strong areas and what needs improvement?
```

**Watch the Memory:** Notice how Luna remembers your preferences, tracks your progress, and personalizes responses!

## Key Concepts

### Memory Tools
Custom tools for state management:
- `remember_topic()` - Store learning topics
- `recall_topics()` - Retrieve past topics
- `record_quiz_score()` - Track assessment results
- `get_learning_progress()` - Generate progress analytics

### State Variables
```python
instruction="""
Current session context:
- Student name: {student_name?}
- Learning style: {learning_style?}
- Current topic: {current_topic?}
"""
```

### Personalization Engine
The agent adapts based on:
- Learning preferences stored in memory
- Past quiz performance
- Topic review patterns
- Session frequency and duration

## Memory Features

### 📊 Progress Analytics
- Total topics learned
- Quiz scores and averages
- Topics needing review
- Learning streak tracking

### 🎯 Adaptive Learning
- Personalized pace adjustment
- Style preferences (visual, hands-on, etc.)
- Difficulty level adaptation
- Review scheduling

### 💾 Persistent State
- Cross-session memory
- Long-term progress tracking
- Preference retention
- Learning history

## What's Next?

In Lab 6, you'll learn about workflow orchestration with sequential, parallel, and loop agents for complex document processing pipelines.

## Tips
- 💡 Try multiple learning sessions to see memory in action
- 💡 Set learning preferences and watch them persist
- 💡 Take quizzes to see progress tracking
- 💡 Notice how responses become more personalized over time
- 💡 Check your learning analytics regularly

## Common Issues
- Memory resets between different agent instances
- State variables show as empty initially (populate through interaction)
- Quiz scores require completing actual quizzes to populate
- Learning preferences need to be explicitly set via conversation