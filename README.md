# Simple Rule-Based Agent

This is a simple rule-based agent that can process text input and perform basic file operations without requiring any external APIs.

## Features

- Text processing and pattern matching
- Basic conversation capabilities
- File operations (read/write)
- Rule-based decision making

## How to Use

1. Make sure you have Python installed on your system
2. Run the agent:
   ```bash
   python simple_agent.py
   ```

3. The agent understands the following types of inputs:
   - Greetings: "hello", "hi", "hey"
   - Farewells: "bye", "goodbye", "see you"
   - Thanks: "thank you", "thanks", "appreciate"
   - Help: "help", "what can you do", "how does this work"

4. Type 'exit' to quit the program

## Example Usage

```
Simple Agent is ready! Type 'exit' to quit.
You: hello
Agent: Hello! How can I help you today?
You: help
Agent: I can help you with:
- Greetings
- Farewells
- Thank you messages
- Basic file operations
```

## Extending the Agent

You can extend the agent's capabilities by:
1. Adding new rules to the `rules` dictionary
2. Adding corresponding responses to the `responses` dictionary
3. Implementing new methods for additional functionality

## File Operations

The agent includes methods for basic file operations:
- `save_to_file(filename, content)`: Saves content to a file
- `read_from_file(filename)`: Reads content from a file 