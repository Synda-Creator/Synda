# synda/ai_core.py
import random
import time


def generate_response(user_input):
    casual_responses = [
        "You don't say! 😲", "That's wild! 🌟", "No way! 😮", "I'm curious, why do you think that? 🤔",
        "Haha, that's funny! 😂", "Seriously? 😳", "Tell me more! 📖", "That's pretty cool. 😎",
        "I hadn't thought of it that way. 🤓", "Wow, interesting! 🤔"
    ]
    targeted_responses = {
        "beautiful": "Yes, it's a lovely day indeed! ☀️",
        "programming": "Programming is such an exciting field! 💻",
        "AI": "AI is definitely the future, can't wait to see what happens next! 🤖",
        "Python": "Python is amazing, I love how versatile it is! 🐍",
        "book": "Finished any good books recently? I’d love some recommendations. 📚"
    }

    for keyword, response in targeted_responses.items():
        if keyword.lower() in user_input.lower():
            return response

    return random.choice(casual_responses)


def process_tweet(tweet):
    user_input = tweet['text']
    ai_response = generate_response(user_input)
    simulate_typing_delay()
    return ai_response


def simulate_typing_delay():
    typing_time = random.uniform(1, 3)  # Simulating typing delay
    time.sleep(typing_time)
