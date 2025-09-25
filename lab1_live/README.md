# Lab 1 Live: Coffee Shop with Voice/Video Streaming 🎙️☕

## Overview
This lab demonstrates the Gemini Live API for real-time voice and video interactions. Experience natural, conversational AI where you can speak directly to your coffee shop assistant and get vocal responses in real-time.

## Learning Objectives
- Experience Gemini Live API capabilities
- Understand real-time streaming interactions
- Learn voice-optimized instruction design
- See the difference between text and voice agent behavior

## Features Demonstrated
- ✅ Gemini Live API (gemini-2.0-flash-live)
- ✅ Real-time voice streaming
- ✅ Bidirectional audio communication
- ✅ Natural conversation patterns
- ✅ Voice-optimized agent personality

## Files
- `agent.py` - Live API enabled coffee shop assistant
- `README.md` - This file

## Requirements
- Webcam and microphone access
- Chrome/Edge browser (for WebRTC support)
- Stable internet connection
- Gemini Live API access

## Running the Lab

```bash
# From the repository root
adk web
```

Then select **lab1_live** from the dropdown and click the **🎙️ Voice** button in the interface.

## Key Differences from Regular Chat

### Voice Interaction Features:
1. **Real-time Response**: No waiting for complete thoughts
2. **Natural Speech Patterns**: Uses conversational filler words
3. **Tone Awareness**: Responds to your vocal energy and mood
4. **Interactive Clarification**: Can interrupt and clarify naturally

### Voice-Optimized Instructions:
- Speak naturally and conversationally
- Use vocal emphasis and enthusiasm
- React to customer's tone and pace
- Handle interruptions gracefully

## Try These Voice Interactions

### 1. Natural Ordering:
- "Hi there! I need something to wake me up this morning"
- "What's good for someone who doesn't usually drink coffee?"
- "I'll take a large latte... actually, make that medium"

### 2. Voice-Specific Features:
- Interrupt the agent mid-sentence to change your order
- Ask questions while the agent is talking
- Use vocal emphasis: "I REALLY need caffeine today!"

### 3. Conversational Flow:
- "What's your favorite drink recommendation?"
- "Tell me about that pumpkin spice latte"
- "I'm in a hurry, what's quick and good?"

## Technical Details

### Model Configuration:
```python
model="gemini-2.0-flash-live"  # Live API compatible model
```

### Voice Optimization:
- Instructions emphasize natural speech patterns
- Personality designed for vocal interaction
- Responsive to real-time conversation flow

### Streaming Benefits:
- **Low Latency**: Near-instant responses
- **Natural Flow**: Interruptions and clarifications
- **Contextual Awareness**: Remembers conversation state
- **Emotional Intelligence**: Responds to vocal cues

## Comparison with Lab 1 (Text)

| Feature | Lab 1 (Text) | Lab 1 Live (Voice) |
|---------|--------------|-------------------|
| Model | gemini-2.0-flash | gemini-2.0-flash-live |
| Interaction | Text-based | Voice/Video |
| Response Time | Complete thoughts | Real-time streaming |
| Interruptions | Not possible | Natural |
| Tone Detection | Text analysis only | Vocal cues |

## What's Next?

In Lab 2, you'll add tools to your agents, making them more capable with:
- Web search capabilities
- Custom function tools
- Multi-tool orchestration

But first, experience the magic of voice AI - it's a completely different interaction paradigm!

## Tips
- 💡 Speak naturally, don't feel like you need to be formal
- 💡 Try interrupting the agent to see real-time response
- 💡 Use different tones (excited, tired, confused) to see how it adapts
- 💡 The agent can handle multiple topics in one conversation
- 💡 Notice how voice interactions feel more natural than text

## Troubleshooting
- **No voice button**: Ensure you're using a supported browser (Chrome/Edge)
- **Microphone not working**: Check browser permissions
- **Poor audio quality**: Check internet connection and microphone setup
- **Agent doesn't respond**: Verify Live API model access in your account