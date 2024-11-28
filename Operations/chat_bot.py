import time
from datetime import datetime
from logger import setup_logger
import json

# Initialize the logger
logger = setup_logger("chat_manager")


class ChatManager:
    def __init__(self, chat_log_file):
        self.chat_log_file = chat_log_file
        self.conversation_history = []

    def log_message(self, sender, message):
        """Log the message to the conversation history and chat log file."""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "sender": sender,
            "message": message,
            "timestamp": timestamp
        }
        self.conversation_history.append(log_entry)
        with open(self.chat_log_file, 'a') as f:
            f.write(json.dumps(log_entry, indent=4) + '\n')
        logger.info(f"Logged message from {sender}: {message}")

    def generate_response(self, user_message):
        """Generate a simple response to the user's message."""
        if "hello" in user_message.lower():
            response = "Hello! How can I assist you today?"
        elif "how are you" in user_message.lower():
            response = "I'm just a bot, but I'm here to help you! How can I assist?"
        elif "help" in user_message.lower():
            response = "Sure, I am here to help. What do you need assistance with?"
        else:
            response = "I'm not sure how to respond to that. Can you please elaborate?"

        return response

    def chat(self, user_message):
        """Handle a chat interaction with the user."""
        self.log_message("User", user_message)
        response = self.generate_response(user_message)
        self.log_message("AgentAyla", response)
        return response


if __name__ == "__main__":
    chat_manager = ChatManager("chat_log.json")

    # Simulating a chat interaction
    print("AgentAyla: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AgentAyla: Goodbye!")
            break
        response = chat_manager.chat(user_input)
        print(f"AgentAyla: {response}")
