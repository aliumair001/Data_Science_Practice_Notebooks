class SimpleAgent:
    def __init__(self):
        self.rules = {
            "greeting": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "see you"],
            "thanks": ["thank you", "thanks", "appreciate"],
            "help": ["help", "what can you do", "how does this work"],
            "save": ["save", "write", "store"],
            "read": ["read", "show", "display"]
        }
        
        self.responses = {
            "greeting": "Hello! How can I help you today?",
            "farewell": "Goodbye! Have a great day!",
            "thanks": "You're welcome!",
            "help": """I can help you with:
- Greetings (try 'hello')
- Farewells (try 'bye')
- Thank you messages (try 'thank you')
- File operations:
  * Save text: Type 'save' followed by your text
  * Read file: Type 'read' followed by filename
  * Example: 'save Hello World' or 'read myfile.txt'""",
            "save": "Please provide the text you want to save (e.g., 'save Hello World')",
            "read": "Please provide the filename to read (e.g., 'read myfile.txt')"
        }
    
    def process_input(self, user_input):
        user_input = user_input.lower().strip()
        
        # Handle file operations
        if user_input.startswith("save "):
            content = user_input[5:]  # Remove 'save ' from the start
            return self.save_to_file("saved_text.txt", content)
        elif user_input.startswith("read "):
            filename = user_input[5:]  # Remove 'read ' from the start
            return self.read_from_file(filename)
        
        # Check for matching rules
        for category, keywords in self.rules.items():
            if any(keyword in user_input for keyword in keywords):
                return self.responses[category]
        
        return "I'm not sure how to respond to that. Type 'help' to see what I can do."

    def save_to_file(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return f"Successfully saved to {filename}"
        except Exception as e:
            return f"Error saving file: {str(e)}"

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

# Example usage
if __name__ == "__main__":
    agent = SimpleAgent()
    
    print("Simple Agent is ready! Type 'exit' to quit.")
    print("Type 'help' to see what I can do!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        response = agent.process_input(user_input)
        print(f"Agent: {response}") 